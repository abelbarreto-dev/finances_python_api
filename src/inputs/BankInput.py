import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class BankInputCreate(BaseModel):
    user_id: uuid.UUID = UpdateValidator.user_id
    code: str = CreateValidator.bank_code
    name: str = CreateValidator.bank_name
    agency: str = CreateValidator.bank_agency
    account_number: str = CreateValidator.bank_account_number
    balance: Decimal = CreateValidator.bank_balance


class ListBankInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    name: Optional[str] = UpdateValidator.bank_name


class BankInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.bank_id
    code: Optional[str] = UpdateValidator.bank_code
    name: Optional[str] = UpdateValidator.bank_name
    agency: Optional[str] = UpdateValidator.bank_agency
    account_number: Optional[str] = UpdateValidator.bank_account_number
    balance: Optional[Decimal] = UpdateValidator.bank_balance
