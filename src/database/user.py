from datetime import datetime
from sqlalchemy import Column, func, Date, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.user import User


class UserRecord(Base):
    __tablename__ = "user"

    user_id = Column(INTEGER, primary_key=True)
    af_id = Column(INTEGER, ForeignKey("af.af_id"), unique=True, nullable=False)
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)
    user_name = Column(VARCHAR, nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    __table_args__ = (UniqueConstraint("user_name"),)

    def __init__(self, user: User):
        self.af_id = user.af_id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.user_name = user.user_name
        self.birth_date = user.birth_date.date()

    def __repr__(self):
        return "<UserRecord(id={self.id!r})>".format(self=self)


def insert(session, user: User):
    session.add(UserRecord(user))
    # session.add(UserRecord(user.af_id, user.first_name, user.last_name, user.user_name, user.birth_date))


def find_by_id(session, user_id: str) -> User:
    pass


def find_by_name(session, user_name: str) -> User:
    pass
