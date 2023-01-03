from sqlalchemy import (Column, func, Sequence, Integer, ForeignKey, CheckConstraint, UniqueConstraint, Index)
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER, BOOLEAN
from metadata_db_constants import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey="users.id", nullable=False)
    text = Column(VARCHAR, nullable=False)
    is_prompt = Column(BOOLEAN, nullable=False)
    is_response = Column(BOOLEAN, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, user_id, text, is_prompt):
        self.user_id = user_id
        self.text = text
        self.is_prompt = is_prompt
        self.is_response = not is_prompt

    def __repr__(self):
        return "<Chat(id={self.id!r})>".format(self=self)
