from typing import List

from sqlalchemy import Column, func, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER, BOOLEAN

from metadata_db_constants import Base
from schema.chat import Chat


class ChatRecord(Base):
    __tablename__ = "chat"

    chat_id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("user.user_id"), nullable=False)
    text = Column(VARCHAR, nullable=False)
    is_prompt = Column(BOOLEAN, nullable=False)
    is_response = Column(BOOLEAN, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )

    def __init__(self, chat: Chat):
        self.user_id = chat.user_id
        self.text = chat.text
        self.is_prompt = chat.is_prompt
        self.is_response = not chat.is_prompt

    def __repr__(self):
        return "<ChatRecord(id={self.id!r})>".format(self=self)


def insert(session, chat: Chat):
    session.add(ChatRecord(chat))


def find_all_by_user_id(session, user_id: str, offset: int, limit: int) -> List[Chat]:
    pass
