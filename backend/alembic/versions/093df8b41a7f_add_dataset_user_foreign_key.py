"""update datasets table

Revision ID: 093df8b41a7f
Revises: d363879b4cc4
Create Date: 2026-08-08 22:26:13.308968
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "093df8b41a7f"
down_revision: Union[str, Sequence[str], None] = "d363879b4cc4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename existing columns instead of adding new NOT NULL columns.
    op.alter_column(
        "datasets",
        "original_name",
        new_column_name="name",
    )

    op.alter_column(
        "datasets",
        "stored_name",
        new_column_name="file_name",
    )

    # Match model definitions.
    op.alter_column(
        "datasets",
        "file_type",
        existing_type=sa.VARCHAR(length=30),
        type_=sa.String(length=50),
        existing_nullable=True,
    )

    op.alter_column(
        "datasets",
        "upload_status",
        existing_type=sa.VARCHAR(length=30),
        type_=sa.String(length=50),
        existing_nullable=False,
    )

    op.alter_column(
        "datasets",
        "storage_path",
        existing_type=sa.VARCHAR(length=500),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "datasets",
        "storage_path",
        existing_type=sa.VARCHAR(length=500),
        nullable=False,
    )

    op.alter_column(
        "datasets",
        "upload_status",
        existing_type=sa.String(length=50),
        type_=sa.VARCHAR(length=30),
        existing_nullable=False,
    )

    op.alter_column(
        "datasets",
        "file_type",
        existing_type=sa.String(length=50),
        type_=sa.VARCHAR(length=30),
        existing_nullable=True,
    )

    op.alter_column(
        "datasets",
        "file_name",
        new_column_name="stored_name",
    )

    op.alter_column(
        "datasets",
        "name",
        new_column_name="original_name",
    )