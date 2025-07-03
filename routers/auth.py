from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User
from security.utils import hash_password, verify_password
from security.auth import create_access_token
from dependencies.utils import get_db
from schemas.user import UserOut, UserCreate

router = APIRouter(tags=["Auth"])

@router.post("/register", response_model=UserOut)
async def register_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where((User.username == user.username) | (User.email == user.username)))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.post("/token")
async def login_user(
    form: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where((User.username == form.username) | (User.email == form.username)))
    user = result.scalar_one_or_none()

    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
