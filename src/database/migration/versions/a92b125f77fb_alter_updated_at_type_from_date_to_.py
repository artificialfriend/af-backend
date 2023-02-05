"""alter updated_at type from date to timestamp

Revision ID: a92b125f77fb
Revises: 1de9708ac399
Create Date: 2023-02-05 23:19:49.952242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a92b125f77fb"
down_revision = "1de9708ac399"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("af", "updated_at", type_=sa.TIMESTAMP, existing_type=sa.Date)


def downgrade() -> None:
    pass
