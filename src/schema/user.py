from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    af_id: str
    email: Optional[str] = None
    first_name: str
    last_name: str
    birth_date: datetime
