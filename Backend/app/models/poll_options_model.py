from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint

class PollOption(SQLModel, table=True):
    __tablename__ = "poll_options"

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    poll_id: int = Field(foreign_key="polls.id", nullable=False)
    option_text: str = Field(max_length=255, nullable=False)
    option_order: int = Field(nullable=False)

    __table_args__ = (
        UniqueConstraint("poll_id", "option_order", name="unique_poll_option_order"),
    )