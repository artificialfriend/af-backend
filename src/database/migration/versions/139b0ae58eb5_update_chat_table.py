"""update chat table

Revision ID: 139b0ae58eb5
Revises: b7b0a9a6de5f
Create Date: 2023-02-04 17:12:29.259062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '139b0ae58eb5'
down_revision = 'b7b0a9a6de5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("chat", "is_response")


def downgrade() -> None:
    pass
