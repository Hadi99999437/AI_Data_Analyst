from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dataset import Dataset


class DatasetRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dataset: Dataset):

        self.db.add(dataset)

        await self.db.commit()

        await self.db.refresh(dataset)

        return dataset

    async def get_by_id(
        self,
        dataset_id: UUID,
    ):

        result = await self.db.execute(
            select(Dataset).where(
                Dataset.id == dataset_id
            )
        )

        return result.scalar_one_or_none()