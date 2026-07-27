from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.repositories.dataset_repository import DatasetRepository
from app.services.dataset_service import DatasetService

from app.schemas.dataset import DatasetResponse

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"],
)


@router.post(
    "/upload",
    response_model=DatasetResponse,
)
async def upload_dataset(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    repo = DatasetRepository(db)

    service = DatasetService(repo)

    dataset = await service.upload_dataset(
        file=file,
        user_id=current_user.id,
    )

    return dataset