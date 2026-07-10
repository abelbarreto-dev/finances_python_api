from pydantic import BaseModel

from src.utils.validators import CreateValidator, UpdateValidator


class UserTypeCreate(BaseModel):
    full_name: CreateValidator.user_full_name
    date_born: CreateValidator.user_date_born
    gender: CreateValidator.user_gender
    cpf: CreateValidator.user_cpf
    email: CreateValidator.user_email
    username: CreateValidator.user_username
    password: CreateValidator.user_password
    phone: CreateValidator.user_phone


class UserTypeLogin(BaseModel):
    username: CreateValidator.user_username
    password: CreateValidator.user_password


class UserTypeUpdate(BaseModel):
    id: UpdateValidator.user_id
    full_name: UpdateValidator.user_full_name
    date_born: UpdateValidator.user_date_born
    gender: UpdateValidator.user_gender
    cpf: UpdateValidator.user_cpf
    email: UpdateValidator.user_email
    username: UpdateValidator.user_username
    phone: UpdateValidator.user_phone
