from fastapi import HTTPException

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(
        self,
        full_name: str,
        email: str,
        password: str,
    ):
        existing = await self.repo.get_by_email(email)

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already exists",
            )

        user = User(
            full_name=full_name,
            email=email,
            password_hash=hash_password(password),
        )

        return await self.repo.create(user)

    async def login(
        self,
        email: str,
        password: str,
    ):
        user = await self.repo.get_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        access_token = create_access_token(
            {"sub": str(user.id)}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }