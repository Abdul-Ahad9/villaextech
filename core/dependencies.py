from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from ..core.security import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from ..models.user import User
from ..schemas.user import TokenData
from ..database import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> User:
    try:
        print("Decoding token...")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = await session.execute(select(User).where(User.username == token_data.username))
    user = user.scalars().first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

def get_current_active_owner(user: User = Depends(get_current_user)):
    if user.role != "owner":
        raise HTTPException(status_code=403, detail="Not authorized as owner")
    return user
