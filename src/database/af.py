from sqlalchemy import Column, func
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.af import AF
from util.dict_util import to_dict


class AFRecord(Base):
    __tablename__ = "af"

    af_id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    skin_color = Column(VARCHAR, nullable=False)
    freckles = Column(VARCHAR, nullable=False)
    hair_color = Column(VARCHAR, nullable=False)
    hair_style = Column(VARCHAR, nullable=False)
    eye_color = Column(VARCHAR, nullable=False)
    eye_lashes = Column(VARCHAR, nullable=False)
    bubble_color = Column(VARCHAR, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )

    def __init__(
        self,
        name: str,
        skin_color: str,
        freckles: str,
        hair_color: str,
        hair_style: str,
        eye_color: str,
        eye_lashes: str,
        bubble_color: str,
    ):

        self.name = name
        self.skin_color = skin_color
        self.freckles = freckles
        self.hair_color = hair_color
        self.hair_style = hair_style
        self.eye_color = eye_color
        self.eye_lashes = eye_lashes
        self.bubble_color = bubble_color

    def __repr__(self):
        return "<AFRecord(id={self.id!r})>".format(self=self)


def insert(session, af: AF):
    session.add(AFRecord(**to_dict(af)))
