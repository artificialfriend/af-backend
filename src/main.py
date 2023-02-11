import logging
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database.metadata_db_dependency import MetadataDbDependency
from schema.af import AF
from schema.chat import Chat
from schema.user import User
from worker import process_chat, store_af_and_user

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

# todo(conscioustahoe): use asyncio


@app.get("/")
async def root():
    return {"response": "welcome to af"}


@app.put("/signup/")
async def sign_up(af: AF, user: User):
    try:
        store_af_and_user(
            metadata_db_dependency=metadata_db_dependency, af=af, user=user
        )
        return {"response": "af and user successfully registered"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@app.get("/af/")
async def af():
    return {"response": "not implemented yet"}


@app.get("/user/")
async def user():
    return {"response": "not implemented yet"}


@app.post("/chat/")
async def chat(user_chat: Chat):
    try:
        last_2_chats = process_chat(
            metadata_db_dependency=metadata_db_dependency, user_chat=user_chat
        )
        return {"response": last_2_chats}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=e.__str__())
