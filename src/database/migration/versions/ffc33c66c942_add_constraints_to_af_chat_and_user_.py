"""add constraints to af, chat and user table

Revision ID: ffc33c66c942
Revises: 5ec994ad29b8
Create Date: 2023-02-05 22:36:19.218989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ffc33c66c942"
down_revision = "5ec994ad29b8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("af", "user_id")
    op.drop_column("af", "name")
    op.drop_column("user", "af_id")
    op.drop_column("chat", "user_id")
    op.alter_column("af", "af_id", type_=sa.VARCHAR, existing_type=sa.Integer)
    op.alter_column("user", "user_id", type_=sa.VARCHAR, existing_type=sa.Integer)
    op.add_column("user", sa.Column("af_id", sa.VARCHAR, nullable=False))
    op.drop_column("user", "user_name")
    op.create_foreign_key("fk_user_af", "user", "af", ["af_id"], ["af_id"])
    op.add_column("chat", sa.Column("user_id", sa.VARCHAR, nullable=False))


def downgrade() -> None:
    pass
