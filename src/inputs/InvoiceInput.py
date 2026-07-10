import uuid
from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.invoice_enum import InvoiceStatus, InvoiceType


class InvoiceInputCreate(BaseModel):
    user_id: uuid.UUID
    name: str
    description: Optional[str] = None
    installments: int
    installs_paid: int
    amount: Decimal
    total_amount: Optional[Decimal] = None
    due_date: date
    invoice_type: InvoiceType
    status: InvoiceStatus


class ListInvoiceInput(BaseModel):
    limit: int
    offset: int
    name: Optional[str] = None
    installments: Optional[int] = None
    due_date: Optional[date] = None
    invoice_type: Optional[InvoiceType] = None
    status: Optional[InvoiceStatus] = None


class InvoiceInputUpdate(BaseModel):
    id: uuid.UUID
    name: Optional[str] = None
    description: Optional[str] = None
    installments: Optional[int] = None
    installs_paid: Optional[int] = None
    amount: Optional[Decimal] = None
    total_amount: Optional[Decimal] = None
    due_date: Optional[date] = None
    invoice_type: Optional[InvoiceType] = None
    status: Optional[InvoiceStatus] = None
