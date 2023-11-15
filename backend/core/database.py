from contextlib import contextmanager
from typing import Generator, List, Optional

from sqlalchemy import create_engine, inspect, pool, Column, Integer, DateTime, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session, sessionmaker

from .config import settings

NAME = settings.SQL_DB
HOST = settings.SQL_HOST
PORT = settings.SQL_PORT
USERNAME = settings.SQL_USERNAME
PASSWORD = settings.SQL_PASSWORD

SQL_URI = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine(
    SQL_URI,
    poolclass=pool.NullPool,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    """SQLAlchemy database model."""

    __name__: str

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def as_dict(self, *, exclude: Optional[List[str]] = None) -> dict:
        """Converts database object to dict.

        Returns:
            dict: Dictionary's row.
        """
        if exclude is None:
            exclude = []
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
            if c.key not in exclude
        }


def get_session() -> Generator:
    """Thread-safe session generator.

    Yields:
        Generator: Thread-safe session.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def session_manager() -> Generator[SessionLocal, None, None]:
    """Thread-safe session generator.

    Yields:
        Generator: Thread-safe session.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()


class SessionManager:  # pragma: no cover
    session: Session

    def __enter__(self):
        self.session = SessionLocal()
        return self.session

    def __exit__(self, *exc_data):
        self.session.close()


def ping_database(session: Session) -> bool:
    try:
        session.execute("SELECT 1")
    except Exception:
        return False
    return True
