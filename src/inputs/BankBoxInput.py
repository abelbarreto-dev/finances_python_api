import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, UpdateValidator


class BankBoxInputCreate(BaseModel):
    bank_id: uuid.UUID
    tag: str = CreateValidator.bank_box_tag
    description: Optional[str] = CreateValidator.bank_box_description
    balance: Decimal


class ListBankBoxInput(BaseModel):
    limit: int
    offset: int
    bank_id: uuid.UUID
    tag: Optional[str] = UpdateValidator.bank_box_tag


class BankBoxInputUpdate(BaseModel):
    id: uuid.UUID
    tag: Optional[str] = UpdateValidator.bank_box_tag
    description: Optional[str] = UpdateValidator.bank_box_description
    balance: Optional[Decimal] = None
