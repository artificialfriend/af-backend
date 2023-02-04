from sqlalchemy import Column, func
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.af import AF


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
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )

    def __init__(self, af: AF):
        self.name = af.name
        self.skin_color = af.skin_color.value
        self.freckles = af.freckles.value
        self.hair_color = af.hair_color.value
        self.hair_style = af.hair_style.value
        self.eye_color = af.eye_color.value
        self.eye_lashes = af.eye_lashes.value

    def __repr__(self):
        return "<AFRecord(id={self.id!r})>".format(self=self)


def insert(session, af: AF):
    session.add(AFRecord(af))
