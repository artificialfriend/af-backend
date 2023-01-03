from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    birth_date_ts: datetime
    af_id: str

    def from_dict(self, d):
        return User(**d)

    def to_dict(self):
        return self.dict()
