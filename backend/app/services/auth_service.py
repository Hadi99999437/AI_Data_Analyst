from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository

from fastapi import HTTPException

from app.core.security import (
    verify_password,
    create_access_token,
)
class AuthService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(
        self,
        full_name,
        email,
        password,
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

        user = await self.user_repo.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }