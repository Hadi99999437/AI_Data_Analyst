from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db

from app.models.user import User

from app.repositories.dataset_repository import DatasetRepository
from app.repositories.analysis_repository import AnalysisRepository

from app.services.analysis_service import AnalysisService

from app.schemas.analysis import (
    AnalysisRequest,
    AnalysisResponse,
)

router = APIRouter(
    tags=["Analysis"],
)


@router.post(
    "/run",
    response_model=AnalysisResponse,
)
async def run_analysis(
    request: AnalysisRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    dataset_repo = DatasetRepository(db)
    analysis_repo = AnalysisRepository(db)

    service = AnalysisService(
        dataset_repo,
        analysis_repo,
    )

    return await service.run_analysis(
        dataset_id=request.dataset_id,
        analysis_type=request.analysis_type,
        user_id=current_user.id,
    )


@router.get(
    "/{job_id}",
    response_model=AnalysisResponse,
)
async def get_analysis(
    job_id: UUID,
    db: AsyncSession = Depends(get_db),
):

    repo = AnalysisRepository(db)

    job = await repo.get_by_id(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found",
        )

    return job