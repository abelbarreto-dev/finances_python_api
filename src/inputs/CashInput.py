import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class CashInputCreate(BaseModel):
    user_id: uuid.UUID = UpdateValidator.user_id
    tag: str = CreateValidator.cash_tag
    description: Optional[str] = CreateValidator.cash_description
    balance: Decimal = CreateValidator.cash_balance


class ListCashInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    tag: Optional[str] = UpdateValidator.cash_tag


class CashInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.cash_id
    tag: Optional[str] = UpdateValidator.cash_tag
    description: Optional[str] = UpdateValidator.cash_description
    balance: Optional[Decimal] = UpdateValidator.cash_balance
