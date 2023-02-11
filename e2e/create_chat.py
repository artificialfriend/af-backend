from database.chat import ChatRecord
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from schema.chat import Chat
from worker import process_chat


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_chat_object():
    chat_dict = {
        "user_id": "Wolf",
        "text": "hello",
        "is_prompt": True,
    }
    chat = Chat(**chat_dict)
    return chat


def create_chat(metadata_db_dependency):
    chat = create_chat_object()
    last_two_chats = process_chat(
        metadata_db_dependency=metadata_db_dependency, user_chat=chat
    )
    print(last_two_chats)


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_chat(metadata_db_dependency)


if __name__ == "__main__":
    run()
