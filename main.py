from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gpt3api

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


@app.get("/")
def root():
    return {"message": "welcome to af"}


@app.get("/chat")
def chat(prompt: str):
    _Gpt3Api_ = gpt3api.Gpt3Api()
    return _Gpt3Api_.generate_essay(prompt)
