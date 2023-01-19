from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
CONNECTION_URL = "postgresql://{}:{}@{}:{}/postgres"
PG_ADVISORY_LOCK_METADATA_DB = 2023
