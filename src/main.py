from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pretrained_transformer.gpt3 import generate_essay
from src.schema.af import AF
from src.schema.chat import Chat
from src.schema.event import Event
from src.schema.user import User

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
    # todo: check request signature, valid user_id, etc. to validate reques
    # todo: use async-await
    return {"message": "welcome to af"}


@app.put("/sign_up")
def sign_up(user: User):
    return {"message": "not implemented yet"}


@app.get("/sign_in")
def sign_in(user: User):
    return {"message": "not implemented yet"}


@app.get("/user")
def user(user: User):
    return {"message": "not implemented yet"}


@app.put("/af")
def af(af: AF):
    return {"message": "not implemented yet"}


@app.post("/chat")
def chat(chat: Chat):
    return generate_essay(chat.text)


@app.get("/chat_history")
def chat_history():
    return {"message": "not implemented yet"}


@app.get("/events")
def get_event(user: User):
    return {"message": "not implemented yet"}


@app.put("/event")
def create_event(event: Event):
    return {"message": "not implemented yet"}
