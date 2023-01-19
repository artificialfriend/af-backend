from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    user_id: Optional[str] = None
    first_name: str
    last_name: str
    user_name: str
    birth_date: datetime
    af_id: str
