import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class CashInputCreate(BaseModel):
    user_id: uuid.UUID
    tag: str
    description: Optional[str] = None
    balance: Decimal


class ListCashInput(BaseModel):
    limit: int
    offset: int
    tag: Optional[str] = None


class CashInputUpdate(BaseModel):
    id: uuid.UUID
    tag: Optional[str] = None
    description: Optional[str] = None
    balance: Optional[Decimal] = None
