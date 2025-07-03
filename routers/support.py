from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from models.core import Support, Work
from schemas.core import SupportCreate, SupportOut
from dependencies.utils import get_db, get_current_user
from models.user import User

router = APIRouter(prefix="/support", tags=["Support"])

@router.post("/", response_model=SupportOut)
async def support_work(
    support: SupportCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if work exists
    result = await db.execute(select(Work).where(Work.id == support.work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")

    new_support = Support(
        work_id=support.work_id,
        supporter_id=current_user.id,
        amount=support.amount
    )

    db.add(new_support)
    await db.commit()
    await db.refresh(new_support)
    return new_support

@router.get("/by-work/{work_id}", response_model=List[SupportOut])
async def get_supports_by_work(work_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Support).where(Support.work_id == work_id))
    return result.scalars().all()

@router.get("/by-user/{user_id}", response_model=List[SupportOut])
async def get_supports_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Support).where(Support.supporter_id == user_id))
    return result.scalars().all()
