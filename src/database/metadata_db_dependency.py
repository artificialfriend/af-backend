import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from metadata_db_constants import Base, PG_ADVISORY_LOCK_METADATA_DB, CONNECTION_URL
from database import user  # noqa


def create_metadata_db_engine():
    connection_url = CONNECTION_URL.format(os.getenv("USER"), os.getenv("PASSWORD"),
                                           os.getenv("HOST"), os.getenv("PORT"))
    engine = create_engine(connection_url, echo=True)
    return engine


class MetadataDbDependency:

    def __init__(self):
        """
        todo: use this as a singleton
        """
        self.engine = create_metadata_db_engine()
        self.instantiate_tables()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def instantiate_tables(self):
        with self.engine.begin() as connection:
            results = connection.execute(f"select pg_try_advisory_lock({PG_ADVISORY_LOCK_METADATA_DB})")
            if results.fetchone()[0]:
                try:
                    Base.metadata.create_all(self.engine)
                finally:
                    connection.execute(f"select pg_try_advisory_unlock({PG_ADVISORY_LOCK_METADATA_DB})")

    def stop(self):
        pass

    def kill(self):
        pass
