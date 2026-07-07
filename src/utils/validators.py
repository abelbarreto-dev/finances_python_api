from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Annotated
from uuid import UUID

from pydantic import AfterValidator, BeforeValidator

from src.utils.bank_utils import (
    is_account_number_validator,
    is_agency_validator,
    is_code_validator,
)
from src.utils.cpf_utils import is_cpf_validator
from src.utils.date_utils import is_date_validator
from src.utils.decimal_utils import is_decimal_validator
from src.utils.email_utils import is_email_validator
from src.utils.gender_enum import GenderType
from src.utils.gender_utils import is_gender_validator
from src.utils.integer_utils import is_integer_validator
from src.utils.phone_utils import is_phone_validator
from src.utils.string_utils import is_string_validator
from src.utils.username_utils import is_username_validator
from src.utils.uuid_utils import is_uuid_validator


@dataclass
class CreateValidator:
    user_full_name = Annotated[str, AfterValidator(is_string_validator("user full_name", 2, 64))]
    user_date_born = Annotated[date, BeforeValidator(is_date_validator("user date_born"))]
    user_gender = Annotated[GenderType, BeforeValidator(is_gender_validator("user gender"))]
    user_cpf = Annotated[str, AfterValidator(is_cpf_validator)]
    user_email = Annotated[str, AfterValidator(is_email_validator)]
    user_username = Annotated[str, AfterValidator(is_username_validator)]
    user_password = Annotated[str, AfterValidator(is_string_validator("user password", 8, 255))]
    user_phone = Annotated[str, AfterValidator(is_phone_validator)]
    cash_tag = Annotated[str, AfterValidator(is_string_validator("cash tag", 2, 32))]
    cash_description = Annotated[
        str | None, AfterValidator(is_string_validator("cash description", 0, 128, True))
    ]
    bank_code = Annotated[str, AfterValidator(is_code_validator)]
    bank_name = Annotated[str, AfterValidator(is_string_validator("bank name", 2, 64))]
    bank_agency = Annotated[str, AfterValidator(is_agency_validator)]
    bank_account_number = Annotated[str, AfterValidator(is_account_number_validator)]
    bank_box_tag = Annotated[str, AfterValidator(is_string_validator("bank box tag", 2, 32))]
    bank_box_description = Annotated[
        str | None, AfterValidator(is_string_validator("bank box description", 0, 128, True))
    ]
    pix_name = Annotated[str, AfterValidator(is_string_validator("pix name", 2, 32))]
    pix_description = Annotated[
        str | None, AfterValidator(is_string_validator("pix description", 0, 128, True))
    ]
    invoice_name = Annotated[str, AfterValidator(is_string_validator("invoice name", 2, 32))]
    invoice_description = Annotated[
        str | None, AfterValidator(is_string_validator("invoice description", 0, 255, True))
    ]
    salary_company = Annotated[
        str | None, AfterValidator(is_string_validator("salary company", 2, 64, True))
    ]
    salary_occupation = Annotated[
        str | None, AfterValidator(is_string_validator("salary occupation", 2, 64, True))
    ]
    salary_salary = Annotated[Decimal, AfterValidator(is_decimal_validator("salary", True))]


@dataclass
class UpdateValidator:
    user_id = Annotated[UUID, BeforeValidator(is_uuid_validator("user id"))]
    user_full_name = Annotated[
        str | None, AfterValidator(is_string_validator("user full_name", 2, 64, True))
    ]
    user_date_born = Annotated[date, BeforeValidator(is_date_validator("user date_born", True))]
    user_gender = Annotated[GenderType, BeforeValidator(is_gender_validator("user gender", True))]
    user_cpf = Annotated[str | None, AfterValidator(is_cpf_validator(True))]
    user_email = Annotated[str | None, AfterValidator(is_email_validator(True))]
    user_username = Annotated[str | None, AfterValidator(is_username_validator(True))]
    user_password = Annotated[
        str | None, AfterValidator(is_string_validator("user password", 8, 255, True))
    ]
    user_phone = Annotated[str | None, AfterValidator(is_phone_validator(True))]
    cash_tag = Annotated[str | None, AfterValidator(is_string_validator("cash tag", 2, 32, None))]
    cash_description = Annotated[
        str | None, AfterValidator(is_string_validator("cash description", 0, 128, True))
    ]
    bank_code = Annotated[str | None, AfterValidator(is_code_validator)]
    bank_name = Annotated[
        str | None, AfterValidator(is_string_validator("bank name", 2, 64, True))
    ]
    bank_agency = Annotated[str | None, AfterValidator(is_agency_validator)]
    bank_account_number = Annotated[str | None, AfterValidator(is_account_number_validator)]
    bank_box_tag = Annotated[
        str | None, AfterValidator(is_string_validator("bank box tag", 2, 32, True))
    ]
    bank_box_description = Annotated[
        str | None, AfterValidator(is_string_validator("bank box description", 0, 128, True))
    ]
    pix_name = Annotated[str | None, AfterValidator(is_string_validator("pix name", 2, 32, True))]
    pix_description = Annotated[
        str | None, AfterValidator(is_string_validator("pix description", 0, 128, True))
    ]
    invoice_name = Annotated[
        str | None, AfterValidator(is_string_validator("invoice name", 2, 32, True))
    ]
    invoice_description = Annotated[
        str | None, AfterValidator(is_string_validator("invoice description", 0, 255, True))
    ]
    salary_id = Annotated[UUID, BeforeValidator(is_uuid_validator("salary id"))]
    salary_company = Annotated[
        str | None, AfterValidator(is_string_validator("salary company", 2, 64, True))
    ]
    salary_occupation = Annotated[
        str | None, AfterValidator(is_string_validator("salary occupation", 2, 64, True))
    ]
    salary_salary = Annotated[Decimal, AfterValidator(is_decimal_validator("salary", True))]
    salary_start_date = Annotated[date, BeforeValidator(is_date_validator("salary start_date"))]
    salary_end_date = Annotated[date, BeforeValidator(is_date_validator("salary end_date"))]


@dataclass
class GetValidator:
    limit = Annotated[int, AfterValidator(is_integer_validator("limit"))]
    offset = Annotated[int, AfterValidator(is_integer_validator("offset"))]
