import logging

from fastapi import HTTPException
from database.chat import ChatRecord
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from pretrained_transformer.gpt3 import get_gpt_3_5_response
from schema.chat import Chat
from util.chat_util import get_chat_context
from util.string_util import remove_prefix

logger = logging.getLogger(__name__)


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_chat_object():
    chat_dict = {"user_id": 1, "text": "was he married?"}
    return Chat(**chat_dict)


def run_chat_flow(metadata_db_dependency):
    user_chat = create_chat_object()
    try:
        with session_context(metadata_db_dependency.get_session()) as session:
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
        return {"response": af_chat.dict(exclude={"chat_id", "behaviour"})}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    chat_response = run_chat_flow(metadata_db_dependency)
    print(f"chat_response: {chat_response}")


if __name__ == "__main__":
    run()
