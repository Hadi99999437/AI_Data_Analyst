from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.chat import ChatRequest, ChatResponse
from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db

from app.repositories.dataset_repository import DatasetRepository
from app.services.chat_service import ChatService

router = APIRouter()


@router.post(
    "",
    response_model=ChatResponse
)
async def chat(
    request: ChatRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):

    dataset_repo = DatasetRepository(db)

    service = ChatService(dataset_repo)

    answer = await service.ask_question(
        dataset_id=request.dataset_id,
        question=request.question,
    )

    return ChatResponse(
        answer=answer
    )