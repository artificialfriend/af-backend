from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: Optional[int] = None
    user_id: int
    text: str
    is_prompt: Optional[bool] = True
    behaviour: Optional[str] = "You are a helpful assistant."
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True
