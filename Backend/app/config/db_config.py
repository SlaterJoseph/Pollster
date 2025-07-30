from sqlalchemy.engine.base import Engine
from sqlmodel import SQLModel, create_engine, Session
from app.models import *
from app.utils.env_handler import env_config

_engine = None


def get_engine() -> Engine:
    global _engine
    db_url = env_config.db_url

    if _engine is None:
        if db_url is None:
            raise ValueError("db_url not set yet")

        # Remove echo true when deploying
        _engine = create_engine(db_url, echo=True)
    return _engine

def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())

def get_session():
    with Session(get_engine()) as session:
        yield session

