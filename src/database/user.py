from datetime import datetime
from sqlalchemy import Column, func, Date, ForeignKey, UniqueConstraint, TEXT
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.user import User


class UserRecord(Base):
    __tablename__ = "user"

    user_id = Column(TEXT, primary_key=True)
    af_id = Column(TEXT, ForeignKey("af.af_id"), unique=True, nullable=False)
    email = Column(TEXT, unique=True, nullable=False)
    first_name = Column(TEXT, nullable=False)
    last_name = Column(TEXT, nullable=False)
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

    __table_args__ = (UniqueConstraint("email"),)

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.af_id = user.af_id
        self.email = user.email
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.birth_date = user.birth_date.date()

    def __repr__(self):
        return "<UserRecord(id={self.id!r})>".format(self=self)


def insert(session, user: User):
    session.add(UserRecord(user))
