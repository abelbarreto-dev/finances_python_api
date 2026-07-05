import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class SalaryInputCreate(BaseModel):
    user_id: uuid.UUID
    company: Optional[str] = None
    occupation: Optional[str] = None
    salary: Optional[Decimal] = None
    activated_at: Optional[datetime] = None


class ListSalaryInput(BaseModel):
    limit: int
    offset: int
    company: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class SalaryInputUpdate(BaseModel):
    id: uuid.UUID
    company: Optional[str] = None
    occupation: Optional[str] = None
    salary: Optional[Decimal] = None
    activated_at: Optional[datetime] = None
