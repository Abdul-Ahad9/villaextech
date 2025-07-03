from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Work
class WorkBase(BaseModel):
    title: str
    description: Optional[str] = None
    content: str

class WorkCreate(WorkBase):
    pass

class WorkOut(WorkBase):
    id: int
    artist_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

# Support
class SupportBase(BaseModel):
    amount: float

class SupportCreate(SupportBase):
    work_id: int

class SupportOut(SupportBase):
    id: int
    work_id: int
    supporter_id: int
    supported_at: datetime

    class Config:
        orm_mode = True
