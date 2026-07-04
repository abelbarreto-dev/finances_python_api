import uuid

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.entities.__base__ import Base
from src.utils.invoice_enum import InvoiceStatus, InvoiceType


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="invoices")

    name = Column(String(32), nullable=False)

    description = Column(String(255), nullable=True)

    installments = Column(Integer, nullable=True, default=1)

    installs_paid = Column(Integer, nullable=True, default=0)

    amount = Column(Numeric(10, 2), nullable=False)

    total_amount = Column(Numeric(10, 2), nullable=True)

    due_date = Column(DateTime, nullable=False)

    invoice_type = Column(Enum(InvoiceType), nullable=False)

    status = Column(Enum(InvoiceStatus), nullable=False, default=InvoiceStatus.PENDING)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
