from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DEFAULT_DATABASE_URL = "sqlite:///./app.db"


def create_sqlite_engine(database_url: str = DEFAULT_DATABASE_URL):
    return create_engine(database_url, connect_args={"check_same_thread": False})


def get_session_factory(engine):
    def _get_session() -> Generator[Session, None, None]:
        session = Session(engine)
        try:
            yield session
        finally:
            session.close()

    return _get_session
