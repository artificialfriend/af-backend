from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: Optional[str] = None
    user_id: int
    text: str
    is_prompt: bool
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
