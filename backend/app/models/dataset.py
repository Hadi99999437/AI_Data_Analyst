from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base_model import BaseModel


class Dataset(Base, BaseModel):
    __tablename__ = "datasets"

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )

    original_name: Mapped[str] = mapped_column(String(255))
    stored_name: Mapped[str] = mapped_column(String(255))

    file_type: Mapped[str] = mapped_column(String(30))
    file_size: Mapped[int] = mapped_column(Integer)

    rows: Mapped[int] = mapped_column(Integer, default=0)
    columns: Mapped[int] = mapped_column(Integer, default=0)

    upload_status: Mapped[str] = mapped_column(
        String(30),
        default="uploaded",
    )

    user = relationship("User", back_populates="datasets")

    analyses = relationship(
        "AnalysisJob",
        back_populates="dataset",
    )