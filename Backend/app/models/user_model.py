from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, field_validator, model_validator, ConfigDict
from typing_extensions import Self
from typing import Optional

from app.security.password import hash_password

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(24), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(1024), nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    photo = Column(String(1024), nullable=True)
    description = Column(String(1024), nullable=True)

class LoginUser(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str

    @field_validator('password', mode='plain')
    @classmethod
    def hashing(cls, value: str) -> str:
        hashed_password = hash_password(value)

    @model_validator(mode='after')
    def require_username_or_email(self) -> Self:
        if self.username is None and self.email is None:
            raise ValueError('Either username or email required')
        return self

class CreateUser(BaseModel):
    username: str
    email: str
    confirm_email: str
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def validate_password(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

    @model_validator(mode='after')
    def validate_email(self) -> Self:
        if self.email != self.confirm_email:
            raise ValueError('Emails do not match')
        return self

class ReturnUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    password: str

