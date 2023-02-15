from datetime import datetime
from sqlalchemy import Column, func, TEXT
from sqlalchemy.dialects.postgresql import TIMESTAMP, INTEGER
from sqlalchemy.orm import relationship
from database.metadata_db_constants import Base
from database.user import UserRecord
from schema.af import AF


class AFRecord(Base):
    __tablename__ = "af"

    af_id = Column(INTEGER, primary_key=True)
    user = relationship("UserRecord", uselist=False)
    name = Column(TEXT, nullable=False)
    skin_color = Column(TEXT, nullable=False)
    freckles = Column(TEXT, nullable=False)
    hair_color = Column(TEXT, nullable=False)
    hair_style = Column(TEXT, nullable=False)
    eye_color = Column(TEXT, nullable=False)
    eye_lashes = Column(TEXT, nullable=False)
    birthday = Column(TEXT, nullable=False)
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __init__(self, af: AF, user: UserRecord = None):
        self.af_id = af.af_id
        self.name = af.name
        self.skin_color = af.skin_color.value
        self.freckles = af.freckles.value
        self.hair_color = af.hair_color.value
        self.hair_style = af.hair_style.value
        self.eye_color = af.eye_color.value
        self.eye_lashes = af.eye_lashes.value
        self.birthday = datetime.now().date()

        if user:
            self.user = user

    def __repr__(self):
        return "<AFRecord(id={self.af_id!r})>".format(self=self)
