from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class InvoiceTypeCreate(BaseModel):
    user_id: UpdateValidator.user_id
    name: CreateValidator.invoice_name
    description: CreateValidator.invoice_description
    installments: CreateValidator.invoice_installments
    installs_paid: CreateValidator.invoice_installs_paid
    amount: CreateValidator.invoice_amount
    total_amount: CreateValidator.invoice_total_amount
    due_date: CreateValidator.invoice_due_date
    invoice_type: CreateValidator.invoice_type
    status: CreateValidator.invoice_status


class ListInvoiceType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    name: UpdateValidator.invoice_name
    installments: UpdateValidator.invoice_installments
    due_date: UpdateValidator.invoice_due_date
    invoice_type: UpdateValidator.invoice_type
    status: UpdateValidator.invoice_status


class InvoiceTypeUpdate(BaseModel):
    id: UpdateValidator.invoice_id
    name: UpdateValidator.invoice_name
    description: UpdateValidator.invoice_description
    installments: UpdateValidator.invoice_installments
    installs_paid: UpdateValidator.invoice_installs_paid
    amount: UpdateValidator.invoice_amount
    total_amount: UpdateValidator.invoice_total_amount
    due_date: UpdateValidator.invoice_due_date
    invoice_type: UpdateValidator.invoice_type
    status: UpdateValidator.invoice_status
