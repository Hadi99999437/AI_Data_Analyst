from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analysis_job import AnalysisJob


class AnalysisRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, job: AnalysisJob):
        self.db.add(job)
        await self.db.commit()
        await self.db.refresh(job)
        return job

    async def get_by_id(self, job_id):
        result = await self.db.execute(
            select(AnalysisJob).where(
                AnalysisJob.id == job_id
            )
        )
        return result.scalar_one_or_none()

    async def update(self, job):
        await self.db.commit()
        await self.db.refresh(job)
        return job