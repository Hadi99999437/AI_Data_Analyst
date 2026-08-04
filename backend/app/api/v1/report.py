from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.dependencies.db import get_analysis_repository

router = APIRouter()


@router.get("/{job_id}")
async def get_report(
    job_id: str,
    repo=Depends(get_analysis_repository),
):

    job = await repo.get_by_id(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found",
        )

    return job.result["report"]