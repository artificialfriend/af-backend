from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventPriority(Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class EventStatus(Enum):
    Not_Started = "Not Started"
    In_Progress = "In Progress"
    Done = "Done"


class EventType(Enum):
    Essay = "Essay"


class Event(BaseModel):
    event_id: Optional[str] = None
    user_id: str
    name: str
    due_date: datetime
    course: str
    event_type: EventType
    priority: EventPriority
    status: EventStatus
