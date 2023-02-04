"""rename event table

Revision ID: 820df50d2c46
Revises: e38e852bd4f2
Create Date: 2023-02-04 18:23:08.707234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "820df50d2c46"
down_revision = "e38e852bd4f2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("event", "doc")


def downgrade() -> None:
    pass
