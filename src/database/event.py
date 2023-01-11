from sqlalchemy import (Column, func, Date, ForeignKey)
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.event import Event
from schema.user import User


class EventTable(Base):
    __tablename__ = "events"

    event_id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("users.user_id"), nullable=False)
    name = Column(VARCHAR, nullable=False)
    course = Column(VARCHAR, nullable=False)
    status = Column(INTEGER, nullable=False)
    priority = Column(INTEGER, nullable=False)
    due_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp())

    def __init__(self, user: User, event: Event):
        self.user_id = user.user_id
        self.name = event.name
        self.course = event.course
        self.due_date = event.due_date.date()
        self.status = event.status.value
        self.priority = event.priority.value

    def __repr__(self):
        return "<Event(id={self.id!r})>".format(self=self)
