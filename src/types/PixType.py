from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class PixTypeCreate(BaseModel):
    bank_id: UpdateValidator.bank_id
    name: CreateValidator.pix_name
    description: CreateValidator.pix_description
    pix_type: CreateValidator.pix_pix_type
    is_mine: CreateValidator.pix_is_mine


class ListPixType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    bank_id: UpdateValidator.bank_filter_id
    name: UpdateValidator.pix_name
    pix_type: UpdateValidator.pix_pix_type
    is_mine: UpdateValidator.pix_is_mine


class PixTypeUpdate(BaseModel):
    id: UpdateValidator.pix_id
    name: UpdateValidator.pix_name
    description: UpdateValidator.pix_description
    pix_type: UpdateValidator.pix_pix_type
    is_mine: UpdateValidator.pix_is_mine
