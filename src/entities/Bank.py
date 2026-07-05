import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.entities.__base__ import Base


class Bank(Base):
    __tablename__ = "banks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )

    user = relationship("User", back_populates="banks")

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    agency: Mapped[str] = mapped_column(String(32), nullable=True)
    account_number: Mapped[str] = mapped_column(String(32), nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=0)

    bank_boxes = relationship("BankBox", back_populates="bank")

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
