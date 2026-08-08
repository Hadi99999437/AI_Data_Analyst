from uuid import uuid4

from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
    )

    name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    file_size: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    rows: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    columns: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    upload_status: Mapped[str] = mapped_column(
        String(50),
        default="uploaded",
    )

    storage_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )