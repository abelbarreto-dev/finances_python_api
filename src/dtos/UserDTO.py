from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.utils.gender_enum import GenderType


class UserDTO(BaseModel):
    id: UUID
    full_name: str
    date_born: date
    gender: GenderType
    cpf: str
    email: str
    username: str
    phone: Optional[str] = None
    created_at: date
