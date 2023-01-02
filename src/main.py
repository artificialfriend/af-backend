from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pretrained_transformers.gpt3 import generate_essay

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

headers = {
    "Content-Type": "application/json"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# todo: use async-await


@app.get("/")
def root():
    return {"message": "welcome to af"}


@app.put("/sign_up")
def sign_up():
    """
    1. check signature
    2. create user, af
    3. return [200, ok]
    """
    return "not implemented yet"


@app.get("/sign_in")
def sign_in():
    """
    1. check signature, user_id, etc.
    2. return [200, ok]
    """
    return "not implemented yet"


@app.get("/user")
def user():
    """
    1. check signature, user_id, etc.
    2. return user
    """
    return "not implemented yet"


@app.get("/af")
def af():
    """
    1. check signature, user_id, etc.
    2. return af
    """
    return "not implemented yet"


@app.get("/chat_history")
def chat_history():
    """
    1. check signature, user_id, etc.
    2. return chat history
    """
    return "not implemented yet"


@app.post("/chat")
def chat(prompt: str):
    return generate_essay(prompt)


@app.get("/event")
def get_event():
    """
    1. check signature, user_id, event_id, etc.
    2. query events
    3. return events
    """
    return "not implemented yet"


@app.put("/event")
def create_event():
    """
    1. check signature, user_id, etc.
    2. insert event
    3. return [200, ok]
    """
    return "not implemented yet"
