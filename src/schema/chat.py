from pydantic import BaseModel


class Chat(BaseModel):
    user_id: str
    text: str
    is_prompt: bool
    is_response: bool

    def to_dict(self):
        return self.dict()


if __name__ == "__main__":
    chat_dict = {
        "user_id": "1",
        "text": "Hello",
        "is_prompt": True,
        "is_response": False,
    }

    chat = Chat(**chat_dict)

    print(chat)
