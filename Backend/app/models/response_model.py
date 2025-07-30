from datetime import datetime

from sqlmodel import SQLModel, Field

class ResponseModel(SQLModel, table=True):
    __tablename__ = "responses"

    user_id: int = Field(foreign_key='users.id', primary_key=True)
    poll_id: int = Field(foreign_key='polls.id', primary_key=True)
    response_id: int = Field(foreign_key='poll_options.id')
    responded_at: datetime | None = Field(default_factory=datetime.now(), nullable=False)