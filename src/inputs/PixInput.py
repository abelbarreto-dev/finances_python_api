import uuid
from typing import Optional

from pydantic import BaseModel

from src.utils.pix_enum import PixType
from src.utils.validators import CreateValidator, UpdateValidator


class PixInputCreate(BaseModel):
    bank_id: uuid.UUID
    name: str = CreateValidator.pix_name
    description: Optional[str] = CreateValidator.pix_description
    pix_type: Optional[PixType] = None
    is_mine: bool


class ListPixInput(BaseModel):
    limit: int
    offset: int
    bank_id: uuid.UUID
    name: Optional[str] = UpdateValidator.pix_name
    pix_type: Optional[PixType] = None
    is_mine: Optional[bool] = None


class PixInputUpdate(BaseModel):
    id: uuid.UUID
    name: Optional[str] = UpdateValidator.pix_name
    description: Optional[str] = UpdateValidator.pix_description
    pix_type: Optional[PixType] = None
    is_mine: Optional[bool] = None
