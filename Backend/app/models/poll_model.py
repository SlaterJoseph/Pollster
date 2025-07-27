from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

class PollCreate(SQLModel):
    question: str
    description: Optional[str] = None
    possible_answers: list[str]
    is_active: bool
    active_until: Optional[datetime] = None
    created_by = Optional[int] = None

class PollResponse(SQLModel):
    id: int
    question: str
    description: Optional[str] = None
    possible_answers: list[str]
    is_active: bool
    created_at: datetime
    active_until: Optional[datetime] = None
    created_by: Optional[int] = None
    likes: int