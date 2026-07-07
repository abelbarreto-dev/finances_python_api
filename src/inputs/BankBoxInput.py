import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class BankBoxInputCreate(BaseModel):
    bank_id: uuid.UUID = UpdateValidator.bank_id
    tag: str = CreateValidator.bank_box_tag
    description: Optional[str] = CreateValidator.bank_box_description
    balance: Decimal = CreateValidator.bank_box_balance


class ListBankBoxInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    bank_id: uuid.UUID = UpdateValidator.bank_id
    tag: Optional[str] = UpdateValidator.bank_box_tag


class BankBoxInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.bank_box_id
    tag: Optional[str] = UpdateValidator.bank_box_tag
    description: Optional[str] = UpdateValidator.bank_box_description
    balance: Optional[Decimal] = UpdateValidator.bank_box_balance
