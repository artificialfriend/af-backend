from database.event import insert
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from schema.event import Event


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_event_object():
    event_dict = {
        "user_id": "4",
        "name": "write an essay on Aegon's ascend",
        "due_date": "2023-01-03 1:10",
        "course": "literature",
        "event_type": "Essay",
        "priority": "Medium",
        "status": "Done",
    }
    event = Event(**event_dict)
    return event


def create_event(metadata_db_dependency):
    event = create_event_object()
    with session_context(metadata_db_dependency.get_session()) as session:
        insert(session=session, event=event)
    print("closing session")


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_event(metadata_db_dependency)


if __name__ == "__main__":
    run()
