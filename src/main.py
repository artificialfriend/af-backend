import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database.af import AFRecord
from database.chat import ChatRecord
from database.metadata_db_dependency import MetadataDbDependency
from database.session_context import session_context
from database.user import UserRecord
from pretrained_transformer.gpt3 import get_gpt_3_response, get_gpt_3_5_response
from schema.af import AF
from schema.chat import Chat
from schema.user import User
from util.chat_util import get_chat_context
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

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

metadata_db_dependency = MetadataDbDependency()

# todo: use asyncio


def is_valid_signature(request_headers):
    # todo: add implementation
    return True


@app.get("/")
async def root():
    return {"response": "af is live!"}


@app.put("/signup/apple/")
async def signup_with_apple(af: AF, user: User):
    try:
        if not is_valid_signature({}):
            raise HTTPException(status_code=403, detail="forbidden")
        with session_context(metadata_db_dependency.get_session()) as session:
            user_record = (
                session.query(UserRecord)
                .filter(UserRecord.apple_user_id == user.apple_user_id)
                .first()
            )
            if user_record is not None:
                raise HTTPException(status_code=400, detail="user already exists")
            session.add(AFRecord(af, user=UserRecord(user=user)))
            session.commit()
            new_user_record = (
                session.query(UserRecord)
                .filter(UserRecord.apple_user_id == user.apple_user_id)
                .first()
            )
            new_user = User.from_orm(new_user_record)
        return {"response": new_user}
    except Exception as e:
        # todo: return raised status code and detail
        raise HTTPException(status_code=500, detail=e.__str__())


@app.get("/signin/apple")
async def signin_with_apple(apple_user_id: str):
    try:
        if not is_valid_signature({}):
            raise HTTPException(status_code=403, detail="forbidden")
        with session_context(metadata_db_dependency.get_session()) as session:
            user_record = (
                session.query(UserRecord)
                .filter(UserRecord.apple_user_id == apple_user_id)
                .first()
            )
            user = User.from_orm(user_record)
        return {"response": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@app.post("/chat/")
async def chat(user_chat: Chat):
    try:
        if not is_valid_signature({}):
            raise HTTPException(status_code=403, detail="forbidden")
        with session_context(metadata_db_dependency.get_session()) as session:
            session.add(ChatRecord(chat=user_chat))
            af_chat = Chat(
                user_id=user_chat.user_id,
                text=remove_prefix(get_gpt_3_response(user_chat.text)),
                is_prompt=False,
                model="text-davinci-003",
            )
            session.add(ChatRecord(chat=af_chat))
        return {"response": af_chat.dict(exclude={"chat_id", "behaviour", "model"})}
    except BaseException:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/chat/turbo")
async def chat_turbo(user_chat: Chat):
    try:
        if not is_valid_signature({}):
            raise HTTPException(status_code=403, detail="forbidden")
        with session_context(metadata_db_dependency.get_session()) as session:
            if not user_chat.is_prompt:
                user_chat.is_prompt = True
            session.add(ChatRecord(chat=user_chat))
            chat_context = get_chat_context(session, user_chat)
            af_chat = Chat(
                user_id=user_chat.user_id,
                text=remove_prefix(get_gpt_3_5_response(context=chat_context)),
                is_prompt=False,
                model="gpt-3.5-turbo",
            )
            session.add(ChatRecord(chat=af_chat))
        return {"response": af_chat.dict(exclude={"chat_id", "behaviour", "model"})}
    except BaseException:
        raise HTTPException(status_code=500, detail="Internal Server Error")
