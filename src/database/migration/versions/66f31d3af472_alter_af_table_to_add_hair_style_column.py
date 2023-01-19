"""alter af table to add hair_style column

Revision ID: 66f31d3af472
Revises: 7ce932a5fe29
Create Date: 2023-01-20 00:10:41.725456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "66f31d3af472"
down_revision = "7ce932a5fe29"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("af", sa.Column("hair_style", sa.VARCHAR))


def downgrade() -> None:
    pass
