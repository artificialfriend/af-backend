from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class EventPriority(Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class EventStatus(Enum):
    Not_Started = "Not Started"
    In_Progress = "In Progress"
    Done = "Done"


class Event(BaseModel):
    name: str
    due_date: datetime
    course: str
    priority: EventPriority
    status: EventStatus

    def to_dict(self):
        return self.dict()


if __name__ == '__main__':
    event_dict = {
        "name": "write an essay on Aegon's ascend",
        "due_date": "2023-01-03 1:10",
        "course": "literature",
        "priority": "Medium",
        "status": "Done"
    }

    event = Event(**event_dict)
