import uuid

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Numeric, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.entities.__base__ import Base
from src.utils.money_enum import MoneyMethod, MoneyType


class MoneyLog(Base):
    __tablename__ = "money_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="money_logs")

    bank_id = Column(UUID(as_uuid=True), ForeignKey("banks.id"), nullable=True)

    bank_box_id = Column(UUID(as_uuid=True), ForeignKey("bank_boxes.id"), nullable=True)

    cash_id = Column(UUID(as_uuid=True), ForeignKey("cashes.id"), nullable=True)

    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), nullable=True)

    type_opp = Column(Enum(MoneyType), nullable=False)

    method_opp = Column(Enum(MoneyMethod), nullable=False)

    amount = Column(Numeric(10, 2), nullable=False, default=0)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
