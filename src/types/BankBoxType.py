from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class BankBoxTypeCreate(BaseModel):
    bank_id: UpdateValidator.bank_id
    tag: CreateValidator.bank_box_tag
    description: CreateValidator.bank_box_description
    balance: CreateValidator.bank_box_balance


class ListBankBoxType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    bank_id: UpdateValidator.bank_id
    tag: UpdateValidator.bank_box_tag


class BankBoxTypeUpdate(BaseModel):
    id: UpdateValidator.bank_box_id
    tag: UpdateValidator.bank_box_tag
    description: UpdateValidator.bank_box_description
    balance: UpdateValidator.bank_box_balance
