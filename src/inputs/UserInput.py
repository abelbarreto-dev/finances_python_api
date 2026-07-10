import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel

from src.utils.gender_enum import GenderType


class UserInputCreate(BaseModel):
    full_name: str
    date_born: date
    gender: GenderType
    cpf: str
    email: str
    username: str
    password: str
    phone: Optional[str] = None


class UserInputLogin(BaseModel):
    username: str
    password: str


class UserInputUpdate(BaseModel):
    id: uuid.UUID
    full_name: Optional[str] = None
    date_born: Optional[date] = None
    gender: Optional[GenderType] = None
    cpf: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    phone: Optional[str] = None
