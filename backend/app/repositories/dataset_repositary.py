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