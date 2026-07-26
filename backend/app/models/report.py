from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base_model import BaseModel


class Report(Base, BaseModel):
    __tablename__ = "reports"

    analysis_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("analysis_jobs.id"),
    )

    report_path: Mapped[str] = mapped_column(String(500))

    report_type: Mapped[str] = mapped_column(String(50))

    analysis = relationship(
        "AnalysisJob",
        back_populates="reports",
    )