from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    user_name: str
    birth_date: datetime
    af_id: str

    def to_dict(self):
        return self.dict()


if __name__ == "__main__":
    user_dict = {
        "user_id": "1",
        "first_name": "Aegon",
        "last_name": "Targaryen",
        "user_name": "JonSnow",
        "birth_date": "2005-05-01 1:10",
        "af_id": "5",
        "key": "value",
    }

    user = User(**user_dict)

    print(user)
