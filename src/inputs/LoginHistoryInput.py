import uuid
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class LoginHistoryInputCreate(BaseModel):
    user_id: uuid.UUID = UpdateValidator.user_id
    login_time: datetime = CreateValidator.login_history_login_time


class ListLoginHistoryInput(BaseModel):
    limit: int = GetValidator.limit
    offset: int = GetValidator.offset
    due_date: Optional[date] = UpdateValidator.login_history_due_date


class LoginHistoryInputUpdate(BaseModel):
    id: uuid.UUID = UpdateValidator.user_id
    logout_time: Optional[datetime] = UpdateValidator.login_history_logout_time
