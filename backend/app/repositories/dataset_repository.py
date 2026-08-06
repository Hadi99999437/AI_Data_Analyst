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



    async def get_all_by_user(self, user_id: UUID):
        result = await self.db.execute(
            select(Dataset)
            .where(Dataset.user_id == user_id)
            .order_by(Dataset.created_at.desc())
        )

        return result.scalars().all()


    async def delete(self, dataset: Dataset):
        await self.db.delete(dataset)
        await self.db.commit()    