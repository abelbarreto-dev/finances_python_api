import uuid

from src.entities.__base__ import Base
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Bank(Base):
    __tablename__ = "banks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="banks")

    code = Column(String(10), nullable=False)

    name = Column(String(64), nullable=False)

    agency = Column(String(32), nullable=True)

    account_number = Column(String(32), nullable=False)

    balance = Column(Numeric(10, 2), nullable=False, default=0)

    bank_boxes = relationship("BankBox", back_populates="bank")

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
