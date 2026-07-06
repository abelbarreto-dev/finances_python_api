import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel

from src.utils.gender_enum import GenderType
from src.utils.validators import CreateValidator, UpdateValidator


class UserInputCreate(BaseModel):
    full_name: str = CreateValidator.user_full_name
    date_born: date
    gender: GenderType
    cpf: str = CreateValidator.user_cpf
    email: str = CreateValidator.user_email
    username: str = CreateValidator.user_username
    password: str = CreateValidator.user_password
    phone: Optional[str] = CreateValidator.user_phone


class UserInputLogin(BaseModel):
    username: str = CreateValidator.user_username
    password: str = CreateValidator.user_password


class UserInputUpdate(BaseModel):
    id: uuid.UUID
    full_name: Optional[str] = UpdateValidator.user_full_name
    date_born: Optional[date] = None
    gender: Optional[GenderType] = None
    cpf: Optional[str] = UpdateValidator.user_cpf
    email: Optional[str] = UpdateValidator.user_email
    username: Optional[str] = UpdateValidator.user_username
    phone: Optional[str] = UpdateValidator.user_phone
