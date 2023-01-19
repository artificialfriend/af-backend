from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from database.user import insert
from schema.user import User


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_user_object():
    user_dict = {
        "af_id": "2",
        "first_name": "Rob",
        "last_name": "Stark",
        "user_name": "Wolf",
        "birth_date": "2005-05-01 1:10",
    }
    user = User(**user_dict)
    return user


def create_user(metadata_db_dependency):
    user = create_user_object()
    with session_context(metadata_db_dependency.get_session()) as session:
        insert(session=session, user=user)


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_user(metadata_db_dependency)


if __name__ == "__main__":
    run()
