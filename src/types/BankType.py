import uuid

from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class BankTypeCreate(BaseModel):
    user_id: UpdateValidator.user_id
    code: CreateValidator.bank_code
    name: CreateValidator.bank_name
    agency: CreateValidator.bank_agency
    account_number: CreateValidator.bank_account_number
    balance: CreateValidator.bank_balance


class ListBankType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    name: UpdateValidator.bank_name


class BankTypeUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.bank_id
    code: UpdateValidator.bank_code
    name: UpdateValidator.bank_name
    agency: UpdateValidator.bank_agency
    account_number: UpdateValidator.bank_account_number
    balance: UpdateValidator.bank_balance
