from datetime import datetime
from typing import Optional

from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.config.db_config import Base

class Poll(Base):
    __tablename__ = 'polls'

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(300))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    ending_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Poll( ID:{self.id!r}, Question:{self.question!r}"