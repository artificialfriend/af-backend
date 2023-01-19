"""add unique constraint on af_id in user

Revision ID: b7b0a9a6de5f
Revises: 66f31d3af472
Create Date: 2023-01-20 02:30:26.327180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b7b0a9a6de5f"
down_revision = "66f31d3af472"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("uq_af_id", "user", ["af_id"])


def downgrade() -> None:
    pass
