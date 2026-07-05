import uuid
from datetime import datetime
from unittest.mock import Base

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.utils.pix_enum import PixType


class Pix(Base):
    __tablename__ = "pixes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    bank_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("banks.id"), nullable=False
    )

    bank = relationship("Bank", back_populates="pixes")

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(String(128), nullable=True)
    pix_type: Mapped[PixType] = mapped_column(Enum(PixType), nullable=False)
    is_mine: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=datetime.now, nullable=False
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
