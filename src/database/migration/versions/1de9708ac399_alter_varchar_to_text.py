"""alter varchar to text

Revision ID: 1de9708ac399
Revises: 68edbaa1f1e7
Create Date: 2023-02-05 23:09:29.370859

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = "1de9708ac399"
down_revision = "68edbaa1f1e7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("user", "user_id", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("user", "af_id", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("user", "email", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("user", "first_name", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("user", "last_name", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("chat", "user_id", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("chat", "text", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "af_id", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "skin_color", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "freckles", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "hair_color", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "hair_style", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "eye_color", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.alter_column("af", "eye_lashes", type_=sa.TEXT, existing_type=sa.VARCHAR)
    op.add_column(
        "af",
        sa.Column(
            "updated_at", sa.Date, nullable=False, server_default=text("CURRENT_DATE")
        ),
    )


def downgrade() -> None:
    pass
