from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base_model import BaseModel


class ChatHistory(Base, BaseModel):
    __tablename__ = "chat_history"

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )

    question: Mapped[str] = mapped_column(Text)

    answer: Mapped[str] = mapped_column(Text)

    user = relationship(
        "User",
        back_populates="chats",
    )