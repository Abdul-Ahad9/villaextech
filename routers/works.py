from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from models.core import Work
from schemas.core import WorkCreate, WorkOut
from dependencies.utils import get_db, get_current_user
from models.user import User

router = APIRouter(prefix="/works", tags=["Works"])

@router.post("/", response_model=WorkOut)
async def create_work(
    work_data: WorkCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_work = Work(**work_data.dict(), artist_id=current_user.id)
    db.add(new_work)
    await db.commit()
    await db.refresh(new_work)
    return new_work

@router.get("/", response_model=List[WorkOut])
async def get_all_works(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Work))
    return result.scalars().all()

@router.get("/{work_id}", response_model=WorkOut)
async def get_single_work(work_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Work).where(Work.id == work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")
    return work

@router.put("/{work_id}", response_model=WorkOut)
async def update_work(work_id: int, updated: WorkCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Work).where(Work.id == work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")
    if work.artist_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this work")
    for key, value in updated.dict().items():
        setattr(work, key, value)
    await db.commit()
    db.refresh(work)
    return work

@router.delete("/{work_id}")
async def delete_work(work_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Work).where(Work.id == work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")
    if work.artist_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this work")
    db.delete(work)
    await db.commit()
    return {"msg": "Work deleted"}
