import logging
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from util.exception_util import (
    HttpError,
    BadRequestError,
    SQLAlchemyIntegrityError,
)


@contextmanager
def session_context(session: Session) -> Session:
    try:
        yield session
        session.commit()
    except HttpError as e:
        session.rollback()
        raise e
    except IntegrityError as e:
        logging.info({"message": f"SQLAlchemy Integrity Error: {e.__str__()}"})
        session.rollback()
        raise SQLAlchemyIntegrityError
    except SQLAlchemyError:
        logging.exception("")
        session.rollback()
        raise BadRequestError()
    except Exception:
        logging.exception("")
        session.rollback()
        raise
    finally:
        session.close()
