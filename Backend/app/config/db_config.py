from typing import Any

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData

from app.models import *
from app.utils.env_handler import env_config

_engine = None

def get_engine() -> Any:
    global _engine

    db_url = env_config.db_url
    # Remove echo when deploying
    _engine = create_engine(db_url, echo=True)
    build_metadata(_engine)
    return _engine

def build_metadata(engine) -> None:
    metadata = MetaData()
    metadata.create_all(engine)

class Base(DeclarativeBase):
    pass

