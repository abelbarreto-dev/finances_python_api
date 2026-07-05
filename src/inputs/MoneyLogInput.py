import uuid
from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.money_enum import MoneyMethod, MoneyType


class MoneyLogInputCreate(BaseModel):
    user_id: uuid.UUID
    bank_id: Optional[uuid.UUID] = None
    bank_box_id: Optional[uuid.UUID] = None
    cash_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    type_opp: MoneyType
    method_opp: MoneyMethod
    amount: Decimal


class ListMoneyLogInput(BaseModel):
    limit: int
    offset: int
    bank_id: Optional[uuid.UUID] = None
    bank_box_id: Optional[uuid.UUID] = None
    cash_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    type_opp: Optional[MoneyType] = None
    method_opp: Optional[MoneyMethod] = None
    due_date: Optional[date] = None


class MoneyLogInputUpdate(BaseModel):
    id: uuid.UUID
    bank_id: Optional[uuid.UUID] = None
    bank_box_id: Optional[uuid.UUID] = None
    cash_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    type_opp: Optional[MoneyType] = None
    method_opp: Optional[MoneyMethod] = None
    amount: Optional[Decimal] = None
