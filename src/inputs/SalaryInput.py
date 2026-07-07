import uuid
from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class SalaryInputCreate(BaseModel):
    user_id: uuid.UUID = UpdateValidator.user_id
    company: Optional[str] = CreateValidator.salary_company
    occupation: Optional[str] = CreateValidator.salary_occupation
    salary: Optional[Decimal] = CreateValidator.salary_salary


class ListSalaryInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    company: Optional[str] = UpdateValidator.salary_company
    start_date: Optional[date] = UpdateValidator.salary_start_date
    end_date: Optional[date] = UpdateValidator.salary_end_date


class SalaryInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.salary_id
    company: Optional[str] = UpdateValidator.salary_company
    occupation: Optional[str] = UpdateValidator.salary_occupation
    salary: Optional[Decimal] = UpdateValidator.salary_salary
