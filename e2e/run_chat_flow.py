from fastapi import HTTPException
from database.chat import ChatRecord
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from database.user import UserRecord
from pretrained_transformer.gpt3 import get_gpt_3_5_response
from schema.chat import Chat
from util.chat_util import get_chat_context, get_last_two_chats
from util.string_util import remove_prefix


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_chat_object():
    chat_dict = {"user_id": 1, "text": "explain how a large language model is trained"}
    return Chat(**chat_dict)


def run_chat_flow(metadata_db_dependency):
    user_chat = create_chat_object()
    try:
        with session_context(metadata_db_dependency.get_session()) as session:
            user = (
                session.query(UserRecord)
                .filter(UserRecord.user_id == user_chat.user_id)
                .first()
            )
            if user is None:
                raise HTTPException(status_code=400, detail={"user not found"})
            if not user_chat.is_prompt:
                user_chat.is_prompt = True
            session.add(ChatRecord(chat=user_chat))
            chat_context = get_chat_context(session, user_chat)
            af_chat = Chat(
                user_id=user_chat.user_id,
                text=remove_prefix(get_gpt_3_5_response(context=chat_context)),
                is_prompt=False,
            )
            session.add(ChatRecord(chat=af_chat))
            session.flush()
            chat_records = get_last_two_chats(session, af_chat)
        last_two_chats = []
        for chat_record in chat_records:
            last_two_chats.append(Chat.from_orm(chat_record))

        return {"response": last_two_chats}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    run_chat_flow(metadata_db_dependency)


if __name__ == "__main__":
    run()
