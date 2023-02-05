from sqlalchemy import Column, func, ForeignKey, TEXT
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, INTEGER
from metadata_db_constants import Base
from schema.af import AF


class AFRecord(Base):
    __tablename__ = "af"

    af_id = Column(INTEGER, primary_key=True)
    skin_color = Column(TEXT, nullable=False)
    freckles = Column(TEXT, nullable=False)
    hair_color = Column(TEXT, nullable=False)
    hair_style = Column(TEXT, nullable=False)
    eye_color = Column(TEXT, nullable=False)
    eye_lashes = Column(TEXT, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __init__(self, af: AF):
        self.af_id = af.af_id
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
