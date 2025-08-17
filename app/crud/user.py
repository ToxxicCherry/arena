from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import User
from app.schemas import UserCreate


async def get_user_by_tg_id(db: AsyncSession, tg_id: int):
    result = await db.execute(select(User).where(User.tg_id==tg_id))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(username=user.username, tg_id=user.tg_id)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()