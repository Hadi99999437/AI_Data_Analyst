from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db

from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import LoginRequest, TokenResponse

from app.models.user import User

router = APIRouter(
    tags=["Authentication"],
)

@router.post(
    "/register",
    response_model=UserResponse,
)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(UserRepository(db))

    return await service.register(
        user.full_name,
        user.email,
        user.password,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    request: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(UserRepository(db))

    return await service.login(
        request.email,
        request.password,
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
async def me(
    current_user: User = Depends(get_current_user),
):
    return current_user