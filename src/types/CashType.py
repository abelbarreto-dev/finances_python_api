from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class CashTypeCreate(BaseModel):
    user_id: UpdateValidator.user_id
    tag: CreateValidator.cash_tag
    description: CreateValidator.cash_description
    balance: CreateValidator.cash_balance


class ListCashType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    tag: UpdateValidator.cash_tag


class CashTypeUpdate(BaseModel):
    id: UpdateValidator.cash_id
    tag: UpdateValidator.cash_tag
    description: UpdateValidator.cash_description
    balance: UpdateValidator.cash_balance
