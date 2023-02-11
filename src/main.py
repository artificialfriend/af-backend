import logging
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database.metadata_db_dependency import MetadataDbDependency
from schema.af import AF
from schema.chat import Chat
from schema.user import User
from worker import process_chat

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

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

metadata_db_dependency = MetadataDbDependency()


@app.get("/")
async def root():
    # todo: only allow requests from an iOS device
    # todo: check request signature, valid user_id, etc. to validate request
    # todo: use async-await
    return {"message": "welcome to af"}


@app.put("/signup/")
async def sign_up(af: AF, user: User):
    try:
        pass
    except Exception:
        pass
    return {"message": "not implemented yet"}


@app.get("/af/")
async def af():
    return {"message": "not implemented yet"}


@app.get("/user/")
async def user():
    return {"message": "not implemented yet"}


@app.post("/chat/")
async def chat(user_chat: Chat):
    try:
        return process_chat(
            metadata_db_dependency=metadata_db_dependency, user_chat=user_chat
        )
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=e.__str__())
