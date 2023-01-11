from sqlalchemy import (Column, func)
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base

from src.schema.af import AF


class AFTable(Base):
    __tablename__ = "afs"

    af_id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    skin_color = Column(VARCHAR, nullable=False)
    freckles = Column(VARCHAR, nullable=False)
    hair_color = Column(VARCHAR, nullable=False)
    eye_color = Column(VARCHAR, nullable=False)
    eye_lashes = Column(VARCHAR, nullable=False)
    bubble_color = Column(VARCHAR, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, af: AF):
        pass

    def __repr__(self):
        return "<Chat(id={self.id!r})>".format(self=self)
