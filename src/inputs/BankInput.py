import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class BankInputCreate(BaseModel):
    user_id: uuid.UUID
    code: str
    name: str
    agency: Optional[str] = None
    account_number: str
    balance: Decimal


class ListBankInput(BaseModel):
    limit: int
    offset: int
    name: Optional[str] = None


class BankInputUpdate(BaseModel):
    id: uuid.UUID
    code: Optional[str] = None
    name: Optional[str] = None
    agency: Optional[str] = None
    account_number: Optional[str] = None
    balance: Optional[Decimal] = None
