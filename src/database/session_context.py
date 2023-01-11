import logging
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from util.exceptions import HttpError, BadRequestError, SQLAlchemyIntegrityError


@contextmanager
def session_context(session):
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
