from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analysis_job import AnalysisJob


class AnalysisRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, analysis):

        self.db.add(analysis)

        await self.db.commit()

        await self.db.refresh(analysis)

        return analysis