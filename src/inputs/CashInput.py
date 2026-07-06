import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, UpdateValidator


class CashInputCreate(BaseModel):
    user_id: uuid.UUID
    tag: str = CreateValidator.cash_tag
    description: Optional[str] = CreateValidator.cash_description
    balance: Decimal


class ListCashInput(BaseModel):
    limit: int
    offset: int
    tag: Optional[str] = UpdateValidator.cash_tag


class CashInputUpdate(BaseModel):
    id: uuid.UUID
    tag: Optional[str] = UpdateValidator.cash_tag
    description: Optional[str] = UpdateValidator.cash_description
    balance: Optional[Decimal] = None
