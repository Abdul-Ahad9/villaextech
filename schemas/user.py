from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime

# User
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=6)

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True