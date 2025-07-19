from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    User Create Model
    """
    username: str
    password: str
    email: str
    description: Optional[str] = None
    photo: Optional[str] = None
    created_at: Optional[datetime] = None


class UserResponse(BaseModel):
    """
    User Response Model
    """
    id: int
    username: str
    password: str
    email: str
    description: Optional[str] = None
    photo: Optional[str] = None
    polls_voted: Optional[int] = None
    created_at: Optional[datetime] = None
