from unittest.mock import Base
import uuid

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.utils.pix_enum import PixType


class Pix(Base):
    __tablename__ = "pixes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    bank_id = Column(UUID(as_uuid=True), ForeignKey("banks.id"), nullable=False)

    bank = relationship("Bank", back_populates="pixes")

    name = Column(String(32), nullable=False)

    description = Column(String(128), nullable=True)

    pix_type = Column(Enum(PixType), nullable=False)

    is_mine = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
