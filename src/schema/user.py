from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    af_id: str
    email: str
    first_name: str
    last_name: str
    birth_date: datetime
