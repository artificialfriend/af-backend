from pydantic import BaseModel


class Chat(BaseModel):
    user_id: str
    text: str
    is_prompt: bool
