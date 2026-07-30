from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db

from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import TokenResponse

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
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(UserRepository(db))

    return await service.login(
        form_data.username,   # username field contains the email
        form_data.password,
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
async def me(
    current_user: User = Depends(get_current_user),
):
    return current_user