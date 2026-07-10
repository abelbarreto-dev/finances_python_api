import uuid
from typing import Optional

from pydantic import BaseModel

from src.utils.pix_enum import PixType


class PixInputCreate(BaseModel):
    bank_id: uuid.UUID
    name: str
    description: Optional[str] = None
    pix_type: Optional[PixType] = None
    is_mine: bool


class ListPixInput(BaseModel):
    limit: int
    offset: int
    bank_id: uuid.UUID
    name: Optional[str] = None
    pix_type: Optional[PixType] = None
    is_mine: Optional[bool] = None


class PixInputUpdate(BaseModel):
    id: uuid.UUID
    name: Optional[str] = None
    description: Optional[str] = None
    pix_type: Optional[PixType] = None
    is_mine: Optional[bool] = None
