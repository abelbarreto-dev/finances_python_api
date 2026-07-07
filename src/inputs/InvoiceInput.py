import uuid
from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.invoice_enum import InvoiceStatus, InvoiceType
from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class InvoiceInputCreate(BaseModel):
    user_id: uuid.UUID = UpdateValidator.user_id
    name: str = CreateValidator.invoice_name
    description: Optional[str] = CreateValidator.invoice_description
    installments: int = CreateValidator.invoice_installments
    installs_paid: int = CreateValidator.invoice_installs_paid
    amount: Decimal = CreateValidator.invoice_amount
    total_amount: Optional[Decimal] = CreateValidator.invoice_total_amount
    due_date: date = CreateValidator.invoice_due_date
    invoice_type: InvoiceType = CreateValidator.invoice_type
    status: InvoiceStatus = CreateValidator.invoice_status


class ListInvoiceInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    name: Optional[str] = UpdateValidator.invoice_name
    installments: Optional[int] = UpdateValidator.invoice_installments
    due_date: Optional[date] = UpdateValidator.invoice_due_date
    invoice_type: Optional[InvoiceType] = UpdateValidator.invoice_type
    status: Optional[InvoiceStatus] = UpdateValidator.invoice_status


class InvoiceInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.invoice_id
    name: Optional[str] = UpdateValidator.invoice_name
    description: Optional[str] = UpdateValidator.invoice_description
    installments: Optional[int] = UpdateValidator.invoice_installments
    installs_paid: Optional[int] = UpdateValidator.invoice_installs_paid
    amount: Optional[Decimal] = UpdateValidator.invoice_amount
    total_amount: Optional[Decimal] = UpdateValidator.invoice_total_amount
    due_date: Optional[date] = UpdateValidator.invoice_due_date
    invoice_type: Optional[InvoiceType] = UpdateValidator.invoice_type
    status: Optional[InvoiceStatus] = UpdateValidator.invoice_status
