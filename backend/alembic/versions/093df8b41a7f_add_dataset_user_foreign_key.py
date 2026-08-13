"""add dataset user foreign key

Revision ID: 093df8b41a7f
Revises: d363879b4cc4
Create Date: 2026-08-08 22:26:13.308968
"""

from typing import Sequence, Union

from alembic import op


revision: str = "093df8b41a7f"
down_revision: Union[str, Sequence[str], None] = "d363879b4cc4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        "fk_datasets_user_id_users",
        "datasets",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_datasets_user_id_users",
        "datasets",
        type_="foreignkey",
    )