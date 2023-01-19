from sqlalchemy import Column, func, Date, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.event import Event
from schema.user import User


class EventRecord(Base):
    __tablename__ = "event"

    event_id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey("user.user_id"), nullable=False)
    event_type = Column(VARCHAR, nullable=False)
    name = Column(VARCHAR, nullable=False)
    course = Column(VARCHAR, nullable=False)
    status = Column(VARCHAR, nullable=False)
    priority = Column(VARCHAR, nullable=False)
    due_date = Column(Date, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __init__(self, event: Event):
        self.user_id = event.user_id
        self.event_type = event.event_type.value
        self.name = event.name
        self.course = event.course
        self.due_date = event.due_date.date()
        self.status = event.status.value
        self.priority = event.priority.value

    def __repr__(self):
        return "<EventRecord(id={self.id!r})>".format(self=self)


def insert(session, event: Event):
    session.add(EventRecord(event))
