"""add nick_names column

Revision ID: c7c30e2017e9
Revises: 
Create Date: 2023-02-25 21:58:17.308156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7c30e2017e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user", sa.Column("nick_names", sa.ARRAY(sa.TEXT), server_default="{human}"))


def downgrade() -> None:
    pass
