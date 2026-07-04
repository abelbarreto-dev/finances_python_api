import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.entities.__base__ import Base


class BankBox(Base):
    __tablename__ = "bank_boxes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    bank_id = Column(UUID(as_uuid=True), ForeignKey("banks.id"), nullable=False)

    bank = relationship("Bank", back_populates="bank_boxes")

    tag = Column(String(32), nullable=False)

    description = Column(String(128), nullable=True)

    balance = Column(Numeric(10, 2), nullable=False, default=0)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
