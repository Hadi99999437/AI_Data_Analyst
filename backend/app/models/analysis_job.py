from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base_model import BaseModel


class AnalysisJob(Base, BaseModel):
    __tablename__ = "analysis_jobs"

    dataset_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("datasets.id"),
    )

    analysis_type: Mapped[str] = mapped_column(
        String(50)
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
    )

    result: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    dataset = relationship(
        "Dataset",
        back_populates="analyses",
    )
    reports = relationship(
    "Report",
    back_populates="analysis",
    )
    