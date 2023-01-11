from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_af(metadata_db_dependency):
    with session_context(metadata_db_dependency.get_session()) as session:
        pass


def create_user(metadata_db_dependency):
    with session_context(metadata_db_dependency.get_session()) as session:
        pass


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_af(metadata_db_dependency)
    create_user(metadata_db_dependency)
