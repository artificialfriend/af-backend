from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: Optional[int]
    af_id: str
    apple_user_id: str
    email: Optional[str]
    given_name: str
    family_name: str
    nick_name: str
    birthday: datetime
