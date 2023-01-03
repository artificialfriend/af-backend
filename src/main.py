from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pretrained_transformer.gpt3 import generate_essay

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
    """
    todo:
        1. use async-await
        2. only allow requests from an iOS device
        3. run uvicorn workers using gunicorn
        4. check request signature, valid user_id, etc. to validate requests 
    """
    return {"message": "welcome to af"}


@app.put("/sign_up")
def sign_up():
    return {"message": "not implemented yet"} 


@app.get("/sign_in")
def sign_in():
    return "not implemented yet"


@app.get("/user")
def user():
    return "not implemented yet"


@app.get("/af")
def af():
    return "not implemented yet"


@app.get("/chat_history")
def chat_history():
    return "not implemented yet"


@app.post("/chat")
def chat(prompt: str):
    return generate_essay(prompt)


@app.get("/event")
def get_event():
    return "not implemented yet"


@app.put("/event")
def create_event():
    return "not implemented yet"
