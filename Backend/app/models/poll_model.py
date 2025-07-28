from datetime import datetime

from sqlmodel import Field, SQLModel

class Poll(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    question: str = Field(nullable=False, max_length=1024)
    created_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)
    ending_at: datetime | None = Field(default=None, nullable=False)
    creator_id: int = Field(foreign_key="users.id", nullable=False)