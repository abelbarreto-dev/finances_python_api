import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, UpdateValidator


class SalaryInputCreate(BaseModel):
    user_id: uuid.UUID
    company: Optional[str] = CreateValidator.salary_company
    occupation: Optional[str] = CreateValidator.salary_occupation
    salary: Optional[Decimal] = None


class ListSalaryInput(BaseModel):
    limit: int
    offset: int
    company: Optional[str] = UpdateValidator.salary_company
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class SalaryInputUpdate(BaseModel):
    id: uuid.UUID
    company: Optional[str] = UpdateValidator.salary_company
    occupation: Optional[str] = UpdateValidator.salary_occupation
    salary: Optional[Decimal] = None
