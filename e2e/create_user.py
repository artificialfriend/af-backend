from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from database.user import UserRecord
from schema.user import User


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_user_object():
    user_dict = {
        "af_id": "1",
        "apple_user_id": "11",
        "email": "klara@afinc.com",
        "given_name": "Aegon",
        "family_name": "Targaryen",
        "nick_name": "Jon",
        "birthday": "2005-02-25 1:10"
    }
    user = User(**user_dict)
    return user


def create_user(metadata_db_dependency):
    user = create_user_object()
    print(user)
    with session_context(metadata_db_dependency.get_session()) as session:
        session.add(UserRecord(user))


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_user(metadata_db_dependency)


if __name__ == "__main__":
    run()
