"""drop doc table

Revision ID: f69a172ef738
Revises: 820df50d2c46
Create Date: 2023-02-04 18:27:42.196813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f69a172ef738"
down_revision = "820df50d2c46"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("doc")


def downgrade() -> None:
    pass
