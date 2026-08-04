from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal

from app.repositories.dataset_repository import DatasetRepository
from app.repositories.user_repository import UserRepository
from app.repositories.analysis_repository import AnalysisRepository


async def get_db():

    async with AsyncSessionLocal() as session:
        yield session


async def get_dataset_repository(
    db: AsyncSession = Depends(get_db),
):
    return DatasetRepository(db)


async def get_user_repository(
    db: AsyncSession = Depends(get_db),
):
    return UserRepository(db)


async def get_analysis_repository(
    db: AsyncSession = Depends(get_db),
):
    return AnalysisRepository(db)