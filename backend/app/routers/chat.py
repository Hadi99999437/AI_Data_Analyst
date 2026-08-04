from fastapi import APIRouter
from fastapi import Depends

from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse

from app.api.dependencies import get_current_user
from app.database.dependencies import get_dataset_repository

from app.services.chat_service import ChatService

router = APIRouter()


@router.post(
    "",
    response_model=ChatResponse
)
async def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user),
    dataset_repo=Depends(get_dataset_repository),
):

    service = ChatService(
        dataset_repo
    )

    answer = await service.ask_question(
        request.dataset_id,
        request.question,
    )

    return ChatResponse(
        answer=answer
    )