from database.chat import insert
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from schema.chat import Chat


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_chat_object():
    chat_dict = {
        "user_id": "1",
        "text": "Reinstated episodic context refers to the process of using past experiences to guide future "
                "decision-making. In particular, it can be used in sampling-based decision-making to help determine "
                "the most likely outcome or reward. By using context from previous episodes, the system can make more "
                "informed decisions, leading to better performance.",
        "is_prompt": False
    }
    chat = Chat(**chat_dict)
    return chat


def create_chat(metadata_db_dependency):
    chat = create_chat_object()
    with session_context(metadata_db_dependency.get_session()) as session:
        insert(session=session, chat=chat)


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_chat(metadata_db_dependency)


if __name__ == '__main__':
    run()
