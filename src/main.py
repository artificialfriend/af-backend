from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pretrained_transformer.gpt3 import generate_essay
from schema.af import AF
from schema.chat import Chat
from schema.user import User
from util.string_util import remove_prefix

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

headers = {"Content-Type": "application/json"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    # todo: only allow requests from an iOS device
    # todo: check request signature, valid user_id, etc. to validate request
    # todo: use async-await
    return {"message": "welcome to af"}


@app.put("/signup/")
def sign_up(af: AF, user: User):
    try:
        pass
    except Exception:
        pass
    return {"message": "not implemented yet"}


@app.get("/af/")
def af():
    return {"message": "not implemented yet"}


@app.get("/user/")
def user():
    return {"message": "not implemented yet"}


@app.post("/chat/")
def chat(chat: Chat):
    response = generate_essay(chat.text)
    response = remove_prefix(response)
    return {"response": response}
