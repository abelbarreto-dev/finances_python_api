import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import UUID, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.entities.__base__ import Base


class Salary(Base):
    __tablename__ = "salary"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )

    user = relationship("User", back_populates="salary")

    company: Mapped[str | None] = mapped_column(String(64), nullable=True)
    occupation: Mapped[str | None] = mapped_column(String(64), nullable=True)
    salary: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    activated_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, default=datetime.now
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
