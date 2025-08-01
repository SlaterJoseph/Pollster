from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, field_validator, model_validator, ConfigDict
from typing_extensions import Self
from typing import Optional

Base = declarative_base()

class ResponseModel(Base):
    __tablename__ = "responses"

    user_id: int = Field(foreign_key='users.id', primary_key=True)
    poll_id: int = Field(foreign_key='polls.id', primary_key=True)
    response_id: int = Field(foreign_key='poll_options.id')
    responded_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)