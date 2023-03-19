from typing import Optional
from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: Optional[int] = None
    user_id: int
    text: str
    is_prompt: Optional[bool] = True
    behaviour: Optional[str] = "You are a helpful assistant."
    model: Optional[str] = "text-davinci-003"

    class Config:
        orm_mode = True
