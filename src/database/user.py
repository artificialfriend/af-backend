from sqlalchemy import (Column, func, Sequence, Integer, ForeignKey, CheckConstraint, UniqueConstraint, Index)
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER, BOOLEAN
from sqlalchemy.orm import relationship
from metadata_db_constants import Base


class UserTable(Base):
    __tablename__ = "users"

    user_id = Column(INTEGER, primary_key=True)
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)
    user_name = Column(VARCHAR, nullable=False, unique=True)
    birth_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())

    __table_args__ = (UniqueConstraint("user_name"))

    def __init__(self, first_name, last_name, user_name, af_id, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.af_id = af_id
        self.birth_date = birth_date  # todo validate birth_date is a timestamp

    def __repr__(self):
        return "<User(id={self.id!r})>".format(self=self)
