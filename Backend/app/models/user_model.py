from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

class UserCreate(SQLModel):
    """
    User Create Model
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    description: Optional[str] = None
    photo: Optional[str] = None
    created_at: Optional[datetime] = None


class UserResponse(SQLModel):
    """
    User Response Model
    """
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    description: Optional[str] = None
    photo: Optional[str] = None
    polls_voted: Optional[int] = None
    created_at: Optional[datetime] = None
