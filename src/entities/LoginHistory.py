import uuid
from datetime import datetime

from sqlalchemy import UUID, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.entities.__base__ import Base


class LoginHistory(Base):
    __tablename__ = "login_history"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    login_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=datetime.now()
    )
    logout_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
