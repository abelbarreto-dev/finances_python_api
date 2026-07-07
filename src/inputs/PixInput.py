import uuid
from typing import Optional

from pydantic import BaseModel

from src.utils.pix_enum import PixType
from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class PixInputCreate(BaseModel):
    bank_id: uuid.UUID = UpdateValidator.bank_id
    name: str = CreateValidator.pix_name
    description: Optional[str] = CreateValidator.pix_description
    pix_type: Optional[PixType] = CreateValidator.pix_pix_type
    is_mine: bool = CreateValidator.pix_is_mine


class ListPixInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    bank_id: uuid.UUID = UpdateValidator.bank_filter_id
    name: Optional[str] = UpdateValidator.pix_name
    pix_type: Optional[PixType] = UpdateValidator.pix_pix_type
    is_mine: Optional[bool] = UpdateValidator.pix_is_mine


class PixInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.pix_id
    name: Optional[str] = UpdateValidator.pix_name
    description: Optional[str] = UpdateValidator.pix_description
    pix_type: Optional[PixType] = UpdateValidator.pix_pix_type
    is_mine: Optional[bool] = UpdateValidator.pix_is_mine
