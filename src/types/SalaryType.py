from pydantic import BaseModel

from src.utils.validators import CreateValidator, GetValidator, UpdateValidator


class SalaryTypeCreate(BaseModel):
    user_id: UpdateValidator.user_id
    company: CreateValidator.salary_company
    occupation: CreateValidator.salary_occupation
    salary: CreateValidator.salary_salary


class ListSalaryType(BaseModel):
    limit: GetValidator.limit
    offset: GetValidator.offset
    company: UpdateValidator.salary_company
    start_date: UpdateValidator.salary_start_date
    end_date: UpdateValidator.salary_end_date


class SalaryTypeUpdate(BaseModel):
    id: UpdateValidator.salary_id
    company: UpdateValidator.salary_company
    occupation: UpdateValidator.salary_occupation
    salary: UpdateValidator.salary_salary
