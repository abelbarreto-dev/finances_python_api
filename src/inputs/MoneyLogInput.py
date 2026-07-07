import uuid
from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.money_enum import MoneyMethod, MoneyType
from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class MoneyLogInputCreate(BaseModel):
    user_id: uuid.UUID = UpdateValidator.user_id
    bank_id: Optional[uuid.UUID] = UpdateValidator.bank_filter_id
    bank_box_id: Optional[uuid.UUID] = UpdateValidator.bank_box_filter_id
    cash_id: Optional[uuid.UUID] = UpdateValidator.cash_filter_id
    invoice_id: Optional[uuid.UUID] = UpdateValidator.invoice_filter_id
    type_opp: MoneyType = CreateValidator.money_log_type
    method_opp: MoneyMethod = CreateValidator.money_log_method
    amount: Decimal = CreateValidator.money_amount


class ListMoneyLogInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    bank_id: Optional[uuid.UUID] = UpdateValidator.bank_filter_id
    bank_box_id: Optional[uuid.UUID] = UpdateValidator.bank_box_filter_id
    cash_id: Optional[uuid.UUID] = UpdateValidator.cash_filter_id
    invoice_id: Optional[uuid.UUID] = UpdateValidator.invoice_filter_id
    type_opp: Optional[MoneyType] = UpdateValidator.money_log_type
    method_opp: Optional[MoneyMethod] = UpdateValidator.money_log_method
    due_date: Optional[date] = UpdateValidator.money_due_date


class MoneyLogInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.money_log_id
    bank_id: Optional[uuid.UUID] = UpdateValidator.bank_filter_id
    bank_box_id: Optional[uuid.UUID] = UpdateValidator.bank_box_filter_id
    cash_id: Optional[uuid.UUID] = UpdateValidator.cash_filter_id
    invoice_id: Optional[uuid.UUID] = UpdateValidator.invoice_filter_id
    type_opp: Optional[MoneyType] = UpdateValidator.money_log_type
    method_opp: Optional[MoneyMethod] = UpdateValidator.money_log_method
    amount: Optional[Decimal] = UpdateValidator.money_amount
