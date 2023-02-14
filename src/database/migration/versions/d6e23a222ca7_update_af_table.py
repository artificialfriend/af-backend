"""update af table

Revision ID: d6e23a222ca7
Revises: a92b125f77fb
Create Date: 2023-02-15 00:41:37.322692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6e23a222ca7'
down_revision = 'a92b125f77fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint(constraint_name="fk_user_af", table_name="user")
    op.alter_column("af", "af_id", type_=sa.INTEGER, existing_type=sa.TEXT, postgresql_using='af_id::integer')
    op.add_column("af", sa.Column("name", sa.TEXT, nullable=False))
    op.add_column("af", sa.Column("birthday", sa.Date, nullable=False))
    op.drop_column("af", "created_at")


def downgrade() -> None:
    pass
