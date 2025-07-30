from datetime import datetime

from sqlmodel import SQLModel, Field

class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id')
    poll_id: int = Field(foreign_key='polls.id')
    comment: str = Field(max_length=256, nullable=False)
    parent_id: int = Field(foreign_key='comments.id')
    created_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)