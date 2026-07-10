from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class LoginHistoryTypeCreate(BaseModel):
    user_id: UpdateValidator.user_id
    login_time: CreateValidator.login_history_login_time


class ListLoginHistoryType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    due_date: UpdateValidator.login_history_due_date


class LoginHistoryTypeUpdate(BaseModel):
    id: UpdateValidator.user_id
    logout_time: UpdateValidator.login_history_logout_time
