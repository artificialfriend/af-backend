from sqlalchemy import (Column, func, Sequence, Integer, ForeignKey, CheckConstraint, UniqueConstraint, Index)
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER, BOOLEAN
from metadata_db_constants import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey="users.id", nullable=False)
    name = Column(VARCHAR, nullable=False)
    course = Column(VARCHAR, nullable=False)
    status = Column(INTEGER, nullable=False)
    priority = Column(INTEGER, nullable=False)
    due_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())

    def __init__(self, user_id, name, course, status, priority, due_date):
        self.user_id = user_id
        self.name = name
        self.course = course
        self.status = status
        self.priority = priority
        self.due_date = due_date  # todo validate birth_date is a timestamp

    def __repr__(self):
        return "<Chat(id={self.id!r})>".format(self=self)
