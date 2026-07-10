import uuid
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class BankBoxInputCreate(BaseModel):
    bank_id: uuid.UUID
    tag: str
    description: Optional[str]
    balance: Decimal


class ListBankBoxInput(BaseModel):
    limit: int
    offset: int
    bank_id: uuid.UUID
    tag: Optional[str] = None


class BankBoxInputUpdate(BaseModel):
    id: uuid.UUID
    tag: Optional[str] = None
    description: Optional[str] = None
    balance: Optional[Decimal] = None
