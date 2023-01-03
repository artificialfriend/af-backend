from sqlalchemy import (Column, func)
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER, BOOLEAN
from metadata_db_constants import Base
from schema.chat import Chat


class ChatTable(Base):
    __tablename__ = "chats"

    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey="users.id", nullable=False)
    text = Column(VARCHAR, nullable=False)
    is_prompt = Column(BOOLEAN, nullable=False)
    is_response = Column(BOOLEAN, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, chat: Chat):
        self.user_id = chat.user_id
        self.text = chat.text
        self.is_prompt = chat.is_prompt
        self.is_response = not chat.is_prompt

    def __repr__(self):
        return "<Chat(id={self.id!r})>".format(self=self)
