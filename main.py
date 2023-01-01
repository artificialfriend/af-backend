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


@app.get("/")
def root():
    return {"message": "welcome to af"}


@app.get("/chat")
def chat(prompt: str):
    gpt3api = Gpt3()
    return gpt3api.generate_essay(prompt)
