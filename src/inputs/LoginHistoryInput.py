import uuid
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class LoginHistoryInputCreate(BaseModel):
    user_id: uuid.UUID
    login_time: datetime


class ListLoginHistoryInput(BaseModel):
    limit: int
    offset: int
    due_date: Optional[date] = None


class LoginHistoryInputUpdate(BaseModel):
    id: uuid.UUID
    logout_time: Optional[datetime] = None
