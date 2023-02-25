from typing import Optional, List

from pydantic import BaseModel

from schema.af import AF


class User(BaseModel):
    user_id: Optional[int]
    af_id: Optional[int]
    af: Optional[AF]
    apple_user_id: str
    email: Optional[str]
    given_name: str
    family_name: str
    nick_names: List[str]
    birthday: str

    class Config:
        orm_mode = True
