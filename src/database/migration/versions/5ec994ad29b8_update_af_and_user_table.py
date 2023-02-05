"""update af and user table

Revision ID: 5ec994ad29b8
Revises: f69a172ef738
Create Date: 2023-02-05 21:42:32.041580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5ec994ad29b8"
down_revision = "f69a172ef738"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user", sa.Column("email", sa.VARCHAR))
    op.create_foreign_key(
        "fk_af_id", "user", "af", ["af_id"], ["af_id"], ondelete="CASCADE"
    )

    op.add_column(
        "af", sa.Column("user_id", sa.INTEGER, nullable=False, server_default="1")
    )
    op.create_foreign_key(
        "fk_user_id", "af", "user", ["user_id"], ["user_id"], ondelete="CASCADE"
    )


def downgrade() -> None:
    pass
