from fastapi import HTTPException
from database.af import AFRecord
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from database.user import UserRecord
from schema.af import AF
from schema.user import User


def get_metadata_db_dependency():
    metadata_db_dependency = MetadataDbDependency()
    return metadata_db_dependency


def create_af_object():
    af_dict = {
        "name": "Ghost",
        "skin_color": "Purple",
        "freckles": "Freckles",
        "hair_color": "White",
        "hair_style": "1",
        "eye_color": "Blue",
        "eye_lashes": "Long",
    }
    af = AF(**af_dict)
    return af


def create_user_object():
    user_dict = {
        "apple_user_id": "6",
        "email": "klara5@afinc.com",
        "given_name": "Aegon",
        "family_name": "Targaryen",
        "nick_names": ["Jon"],
        "birthday": "2005-02-25",
    }
    user = User(**user_dict)
    return user


def run_signup_flow(metadata_db_dependency):
    af = create_af_object()
    user = create_user_object()
    try:
        with session_context(metadata_db_dependency.get_session()) as session:
            user_record = (
                session.query(UserRecord)
                .filter(UserRecord.apple_user_id == user.apple_user_id)
                .first()
            )
            if user_record is not None:
                raise HTTPException(status_code=400, detail="user already exists")
            session.add(AFRecord(af, user=UserRecord(user=user)))
            session.commit()
            new_user_record = (
                session.query(UserRecord)
                .filter(UserRecord.apple_user_id == user.apple_user_id)
                .first()
            )
            new_user = User.from_orm(new_user_record)
        return {"response": new_user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


def run():
    metadata_db_dependency = get_metadata_db_dependency()
    run_signup_flow(metadata_db_dependency)


if __name__ == "__main__":
    run()
