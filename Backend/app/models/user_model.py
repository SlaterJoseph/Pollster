from typing import Optional

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    description: Optional[str] = None
    photo: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    password: str
    email: str
    description: Optional[str] = None
    photo: Optional[str] = None
    polls_voted: Optional[int] = None
