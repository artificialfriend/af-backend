import logging
from fastapi import HTTPException

from database.af import AFRecord
from database.chat import ChatRecord
from database.session_context import session_context
from database.user import UserRecord
from pretrained_transformer.gpt3 import get_gpt_response
from schema.af import AF
from schema.chat import Chat
from schema.user import User
from util.string_util import remove_prefix

logger = logging.getLogger(__name__)


def process_chat(metadata_db_dependency, user_chat: Chat):
    last_two_chats = []
    with session_context(metadata_db_dependency.get_session()) as session:
        user = (
            session.query(UserRecord)
            .filter(UserRecord.user_id == user_chat.user_id)
            .first()
        )
        if user is None:
            raise HTTPException(status_code=400, detail={"user not found"})
        session.add(ChatRecord(chat=user_chat))
        af_chat = Chat(
            user_id=user_chat.user_id,
            text=remove_prefix(get_gpt_response(user_chat.text)),
            is_prompt=False,
        )
        session.add(ChatRecord(chat=af_chat))
        session.commit()
        chat_records = (
            session.query(ChatRecord)
            .filter(ChatRecord.user_id == af_chat.user_id)
            .order_by(ChatRecord.created_at.desc())
            .limit(2)
        )
    for chat_record in chat_records:
        last_two_chats.append(Chat.from_orm(chat_record))
    return last_two_chats


def store_af_and_user(metadata_db_dependency, af: AF, user: User):
    with session_context(metadata_db_dependency.get_session()) as session:
        session.add(AFRecord(af))
        session.add(UserRecord(user))
