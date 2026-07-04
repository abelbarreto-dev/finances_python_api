from unittest.mock import Base
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Cash(Base):
    __tablename__ = "cashes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="cashes")

    tag = Column(String(32), nullable=False)

    description = Column(String(128), nullable=True)

    balance = Column(Numeric(10, 2), nullable=False, default=0)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
