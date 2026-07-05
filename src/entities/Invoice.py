import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.entities.__base__ import Base
from src.utils.invoice_enum import InvoiceStatus, InvoiceType


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )

    user = relationship("User", back_populates="invoices")

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    installments: Mapped[int] = mapped_column(Integer, nullable=True, default=1)
    installs_paid: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    invoice_type: Mapped[InvoiceType] = mapped_column(Enum(InvoiceType), nullable=False)
    status: Mapped[InvoiceStatus] = mapped_column(
        Enum(InvoiceStatus), nullable=False, default=InvoiceStatus.PENDING
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
