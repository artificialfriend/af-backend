"""add foreign key contraint in chat table

Revision ID: 68edbaa1f1e7
Revises: ffc33c66c942
Create Date: 2023-02-05 23:04:11.271914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68edbaa1f1e7'
down_revision = 'ffc33c66c942'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key("fk_chat_user", "chat", "user", ["user_id"], ["user_id"])


def downgrade() -> None:
    pass
