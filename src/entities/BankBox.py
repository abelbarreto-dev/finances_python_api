import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.entities.__base__ import Base


class BankBox(Base):
    __tablename__ = "bank_boxes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    bank_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("banks.id"), nullable=False
    )

    bank = relationship("Bank", back_populates="bank_boxes")

    tag: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(String(128), nullable=True)
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
