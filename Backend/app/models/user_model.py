from datetime import datetime

from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=20)
    email: str = Field(max_length=50)
    hashed_password: str = Field(max_length=1024)
    created_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)
    photo: str = Field(max_length=1024)
    description: str = Field(max_length=1024)
