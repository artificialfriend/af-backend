from sqlalchemy import Column, func, ForeignKey, TEXT, INTEGER
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from database.metadata_db_constants import Base
from schema.user import User


class UserRecord(Base):
    __tablename__ = "user"

    user_id = Column(INTEGER, primary_key=True)
    apple_user_id = Column(TEXT, unique=True, nullable=True)
    af_id = Column(
        INTEGER, ForeignKey("af.af_id", ondelete="CASCADE"), unique=True, nullable=False
    )
    af = relationship("AFRecord", back_populates="user")
    email = Column(TEXT, unique=True, nullable=False)
    given_name = Column(TEXT, nullable=False)
    family_name = Column(TEXT, nullable=False)
    nick_name = Column(TEXT, nullable=False)
    birthday = Column(TEXT, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.af_id = user.af_id
        self.apple_user_id = user.apple_user_id
        self.email = user.email
        self.given_name = user.given_name
        self.family_name = user.family_name
        self.nick_name = user.nick_name
        self.birthday = user.birthday

    def __repr__(self):
        return "<UserRecord(id={self.user_id!r})>".format(self=self)
