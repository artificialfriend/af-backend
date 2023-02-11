from sqlalchemy import Column, func, ForeignKey, TEXT
from sqlalchemy.dialects.postgresql import TIMESTAMP, INTEGER, BOOLEAN
from database.metadata_db_constants import Base
from schema.chat import Chat


class ChatRecord(Base):
    __tablename__ = "chat"

    chat_id = Column(INTEGER, primary_key=True)
    user_id = Column(TEXT, ForeignKey("user.user_id"), nullable=False)
    text = Column(TEXT, nullable=False)
    is_prompt = Column(BOOLEAN, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )

    def __init__(self, chat: Chat):
        self.user_id = chat.user_id
        self.text = chat.text
        self.is_prompt = chat.is_prompt

    def __repr__(self):
        return "<ChatRecord(id={self.id!r})>".format(self=self)
