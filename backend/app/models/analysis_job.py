from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base_model import BaseModel


class AnalysisJob(Base, BaseModel):
    __tablename__ = "analysis_jobs"

    dataset_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("datasets.id"),
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="completed",
    )

    result_json: Mapped[dict] = mapped_column(JSON)

    dataset = relationship(
        "Dataset",
        back_populates="analyses",
    )

    user = relationship(
        "User",
    )