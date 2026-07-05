import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.entities.__base__ import Base
from src.utils.money_enum import MoneyMethod, MoneyType


class MoneyLog(Base):
    __tablename__ = "money_logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )

    user = relationship("User", back_populates="money_logs")

    bank_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=True)
    bank_box_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=True)
    cash_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=True)
    invoice_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=True)

    type_opp: Mapped[MoneyType] = mapped_column(Enum(MoneyType), nullable=False)
    method_opp: Mapped[MoneyMethod] = mapped_column(Enum(MoneyMethod), nullable=False)

    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
