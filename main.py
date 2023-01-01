from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pretrained_transformers.gpt3 import Gpt3

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

# GET Requests


@app.get("/")
def root():
    return {"message": "welcome to af"}


@app.get("/chat")
def chat(prompt: str):
    gpt3 = Gpt3()
    return gpt3.generate_essay(prompt)


@app.get("/user")
def get_user():
    return "not implemented yet"


@app.get("/event")
def get_event():
    return "not implemented yet"

# PUT Requests


@app.put("/user")
def create_user():
    return "not implemented yet"


@app.put("/event")
def create_event():
    return "not implemented yet"

