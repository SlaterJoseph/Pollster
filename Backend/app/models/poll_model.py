from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class PollCreate(BaseModel):
    question: str
    description: Optional[str] = None
    possible_answers: list[str]
    is_active: bool
    active_until: Optional[datetime] = None
    created_by = Optional[int] = None

class PollResponse(BaseModel):
    id: int
    question: str
    description: Optional[str] = None
    possible_answers: list[str]
    is_active: bool
    created_at: datetime
    active_until: Optional[datetime] = None
    created_by: Optional[int] = None
    likes: int