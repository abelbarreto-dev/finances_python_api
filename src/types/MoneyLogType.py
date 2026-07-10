from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class MoneyLogInputCreate(BaseModel):
    user_id: UpdateValidator.user_id
    bank_id: UpdateValidator.bank_filter_id
    bank_box_id: UpdateValidator.bank_box_filter_id
    cash_id: UpdateValidator.cash_filter_id
    invoice_id: UpdateValidator.invoice_filter_id
    type_opp: CreateValidator.money_log_type
    method_opp: CreateValidator.money_log_method
    amount: CreateValidator.money_amount


class ListMoneyLogInput(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    bank_id: UpdateValidator.bank_filter_id
    bank_box_id: UpdateValidator.bank_box_filter_id
    cash_id: UpdateValidator.cash_filter_id
    invoice_id: UpdateValidator.invoice_filter_id
    type_opp: UpdateValidator.money_log_type
    method_opp: UpdateValidator.money_log_method
    due_date: UpdateValidator.money_due_date


class MoneyLogInputUpdate(BaseModel):
    id: UpdateValidator.money_log_id
    bank_id: UpdateValidator.bank_filter_id
    bank_box_id: UpdateValidator.bank_box_filter_id
    cash_id: UpdateValidator.cash_filter_id
    invoice_id: UpdateValidator.invoice_filter_id
    type_opp: UpdateValidator.money_log_type
    method_opp: UpdateValidator.money_log_method
    amount: UpdateValidator.money_amount
