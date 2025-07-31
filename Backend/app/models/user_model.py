from datetime import datetime
from typing_extensions import Self
from sqlmodel import SQLModel, Field
from pydantic import model_validator, ValidationError, field_validator
from app.security.password import verify_password, hash_password

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=20)
    email: str = Field(max_length=50)
    password: str = Field(max_length=1024)
    created_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)
    photo: str = Field(max_length=1024)
    description: str = Field(max_length=1024)

class LoginUser(SQLModel):
    username: str | None = Field(default=None, max_length=20)
    email: str | None = Field(default=None, max_length=50)
    password: str = Field(max_length=1024)

    @field_validator('password', mode='plain')
    @classmethod
    def hashing(cls, value: str) -> str:
        hashed_password = hash_password(value)

    @model_validator(mode='after')
    def require_username_or_email(self) -> Self:
        if self.username is None and self.email is None:
            raise ValidationError('Either username or email required')
        return self

class CreateUser(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=20)
    email: str = Field(max_length=50)
    confirm_email: str = Field(max_length=50)
    password: str = Field(max_length=1024)
    confirm_password: str = Field(max_length=1024)
    created_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)

    @model_validator(mode='after')
    def validate_password(self) -> Self:
        if self.password != self.confirm_password:
            raise ValidationError('Passwords do not match')
        return self

    @model_validator(mode='after')
    def validate_password(self) -> Self:
        if self.email != self.confirm_email:
            raise ValidationError('Emails do not match')
        return self
