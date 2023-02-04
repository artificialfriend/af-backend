"""remove bubble color column

Revision ID: e38e852bd4f2
Revises: 139b0ae58eb5
Create Date: 2023-02-04 17:54:29.401083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e38e852bd4f2'
down_revision = '139b0ae58eb5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("af", "bubble_color")


def downgrade() -> None:
    pass
