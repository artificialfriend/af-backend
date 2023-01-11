from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_chat(metadata_db_dependency):
    with session_context(metadata_db_dependency.get_session()) as session:
        pass


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_chat(metadata_db_dependency)