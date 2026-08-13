from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base_model import BaseModel


class User(Base, BaseModel):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String(150),
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    datasets = relationship(
        "Dataset",
        back_populates="user",
    )

    chats = relationship(
        "ChatHistory",
        back_populates="user",
    )