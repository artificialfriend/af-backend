from database.af import insert
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from schema.af import AF


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_af_object():
    af_dict = {
        "af_id": "Klara#1",
        "skin_color": "Caramel",
        "freckles": "Few",
        "hair_color": "White",
        "hair_style": "Wavy",
        "eye_color": "Hazel",
        "eye_lashes": "Straight",
    }
    af = AF(**af_dict)
    return af


def create_af_record(metadata_db_dependency):
    af = create_af_object()
    with session_context(metadata_db_dependency.get_session()) as session:
        insert(session=session, af=af)


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    create_af_record(metadata_db_dependency)


if __name__ == "__main__":
    run()
