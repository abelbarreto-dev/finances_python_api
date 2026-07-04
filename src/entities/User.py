import uuid

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.entities.__base__ import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    full_name = Column(String(64), nullable=False)

    email = Column(String(255), nullable=False, unique=True)

    username = Column(String(64), nullable=False, unique=True)

    password = Column(String(255), nullable=False)

    phone = Column(String(20), nullable=True)

    banks = relationship("Bank", back_populates="user")
    cashes = relationship("Cash", back_populates="user")
    invoices = relationship("Invoice", back_populates="user")

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    deleted_at = Column(DateTime, nullable=True)
