from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Annotated
from uuid import UUID

from pydantic import AfterValidator, BeforeValidator

from src.utils.bank_utils import (
    is_account_number_validator,
    is_agency_validator,
    is_code_validator,
)
from src.utils.boolean_utils import is_boolean_validator
from src.utils.cpf_utils import is_cpf_validator
from src.utils.date_utils import is_date_validator
from src.utils.datetime_utils import is_datetime_validator
from src.utils.decimal_utils import is_decimal_validator
from src.utils.email_utils import is_email_validator
from src.utils.gender_enum import GenderType
from src.utils.gender_utils import is_gender_validator
from src.utils.integer_utils import is_integer_validator
from src.utils.invoice_enum import InvoiceStatus, InvoiceType
from src.utils.invoice_utils import is_invoice_status_validator, is_invoice_type_validator
from src.utils.money_enum import MoneyMethod, MoneyType
from src.utils.money_utils import is_money_method_validator, is_money_type_validator
from src.utils.phone_utils import is_phone_validator
from src.utils.pix_enum import PixType
from src.utils.pix_utils import is_pix_validator
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
    cash_balance = Annotated[Decimal, AfterValidator(is_decimal_validator("cash balance"))]
    bank_code = Annotated[str, AfterValidator(is_code_validator)]
    bank_name = Annotated[str, AfterValidator(is_string_validator("bank name", 2, 64))]
    bank_agency = Annotated[str, AfterValidator(is_agency_validator)]
    bank_account_number = Annotated[str, AfterValidator(is_account_number_validator)]
    bank_balance = Annotated[Decimal, AfterValidator(is_decimal_validator("bank balance"))]
    bank_box_tag = Annotated[str, AfterValidator(is_string_validator("bank box tag", 2, 32))]
    bank_box_description = Annotated[
        str | None, AfterValidator(is_string_validator("bank box description", 0, 128, True))
    ]
    bank_box_balance = Annotated[
        Decimal, AfterValidator(is_decimal_validator("bank box balance"))
    ]
    login_history_login_time = Annotated[
        datetime, BeforeValidator(is_datetime_validator("login history login time"))
    ]
    money_log_type = Annotated[
        MoneyType, BeforeValidator(is_money_type_validator("money log type enum"))
    ]
    money_log_method = Annotated[
        MoneyMethod, BeforeValidator(is_money_method_validator("money log method enum"))
    ]
    money_amount = Annotated[Decimal, AfterValidator(is_decimal_validator("money amount"))]
    pix_name = Annotated[str, AfterValidator(is_string_validator("pix name", 2, 32))]
    pix_description = Annotated[
        str | None, AfterValidator(is_string_validator("pix description", 0, 128, True))
    ]
    pix_is_mine = Annotated[bool, BeforeValidator(is_boolean_validator("pix is_mine"))]
    pix_pix_type = Annotated[PixType, BeforeValidator(is_pix_validator("pix pix type"))]
    invoice_name = Annotated[str, AfterValidator(is_string_validator("invoice name", 2, 32))]
    invoice_description = Annotated[
        str | None, AfterValidator(is_string_validator("invoice description", 0, 255, True))
    ]
    invoice_due_date = Annotated[date, BeforeValidator(is_date_validator("invoice due_date"))]
    invoice_installments = Annotated[
        int, AfterValidator(is_integer_validator("invoice installment"))
    ]
    invoice_installs_paid = Annotated[
        int, AfterValidator(is_integer_validator("invoice installs paid"))
    ]
    invoice_amount = Annotated[Decimal, AfterValidator(is_decimal_validator("invoice amount"))]
    invoice_total_amount = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("invoice amount", True))
    ]
    invoice_status = Annotated[
        InvoiceStatus, BeforeValidator(is_invoice_status_validator("invoice status"))
    ]
    invoice_type = Annotated[
        InvoiceType, BeforeValidator(is_invoice_type_validator("invoice type"))
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
    cash_id = Annotated[UUID, BeforeValidator(is_uuid_validator("cash id"))]
    cash_filter_id = Annotated[UUID, BeforeValidator(is_uuid_validator("cash id", True))]
    cash_tag = Annotated[str | None, AfterValidator(is_string_validator("cash tag", 2, 32, True))]
    cash_description = Annotated[
        str | None, AfterValidator(is_string_validator("cash description", 0, 128, True))
    ]
    cash_balance = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("cash balance", True))
    ]
    bank_id = Annotated[UUID, BeforeValidator(is_uuid_validator("bank id"))]
    bank_filter_id = Annotated[UUID, BeforeValidator(is_uuid_validator("bank id", True))]
    bank_code = Annotated[str | None, AfterValidator(is_code_validator)]
    bank_name = Annotated[
        str | None, AfterValidator(is_string_validator("bank name", 2, 64, True))
    ]
    bank_agency = Annotated[str | None, AfterValidator(is_agency_validator)]
    bank_account_number = Annotated[str | None, AfterValidator(is_account_number_validator)]
    bank_balance = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("bank balance", True, True))
    ]
    bank_box_id = Annotated[UUID, BeforeValidator(is_uuid_validator("bank box id"))]
    bank_box_filter_id = Annotated[UUID, BeforeValidator(is_uuid_validator("bank box id", True))]
    bank_box_tag = Annotated[
        str | None, AfterValidator(is_string_validator("bank box tag", 2, 32, True))
    ]
    bank_box_description = Annotated[
        str | None, AfterValidator(is_string_validator("bank box description", 0, 128, True))
    ]
    bank_box_balance = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("bank box balance", True, True))
    ]
    login_history_due_date = Annotated[
        date | None, BeforeValidator(is_date_validator("login history due_date", True))
    ]
    login_history_login_time = Annotated[
        datetime | None, BeforeValidator(is_datetime_validator("login history login time", True))
    ]
    login_history_logout_time = Annotated[
        datetime | None, BeforeValidator(is_datetime_validator("login history logout time", True))
    ]
    money_log_id = Annotated[UUID, BeforeValidator(is_uuid_validator("money log id"))]
    money_log_type = Annotated[
        MoneyType | None, BeforeValidator(is_money_type_validator("money log type enum", True))
    ]
    money_log_method = Annotated[
        MoneyMethod | None,
        BeforeValidator(is_money_method_validator("money log method enum", True)),
    ]
    money_due_date = Annotated[date, BeforeValidator(is_date_validator("money due_date", True))]
    money_amount = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("money amount", True))
    ]
    pix_id = Annotated[UUID, BeforeValidator(is_uuid_validator("pix id"))]
    pix_name = Annotated[str | None, AfterValidator(is_string_validator("pix name", 2, 32, True))]
    pix_description = Annotated[
        str | None, AfterValidator(is_string_validator("pix description", 0, 128, True))
    ]
    pix_is_mine = Annotated[
        bool | None, BeforeValidator(is_boolean_validator("pix is_mine", True))
    ]
    pix_pix_type = Annotated[
        PixType | None, BeforeValidator(is_pix_validator("pix pix type", True))
    ]
    invoice_id = Annotated[UUID, BeforeValidator(is_uuid_validator("invoice id"))]
    invoice_filter_id = Annotated[UUID, BeforeValidator(is_uuid_validator("invoice id", True))]
    invoice_name = Annotated[
        str | None, AfterValidator(is_string_validator("invoice name", 2, 32, True))
    ]
    invoice_description = Annotated[
        str | None, AfterValidator(is_string_validator("invoice description", 0, 255, True))
    ]
    invoice_due_date = Annotated[
        date | None, BeforeValidator(is_date_validator("invoice due_date", True))
    ]
    invoice_installments = Annotated[
        int | None, AfterValidator(is_integer_validator("invoice installments", True))
    ]
    invoice_installs_paid = Annotated[
        int | None, AfterValidator(is_integer_validator("invoice installs paid", True))
    ]
    invoice_status = Annotated[
        InvoiceStatus | None, BeforeValidator(is_invoice_status_validator("invoice status", True))
    ]
    invoice_type = Annotated[
        InvoiceType | None, BeforeValidator(is_invoice_type_validator("invoice type", True))
    ]
    invoice_amount = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("invoice amount", True))
    ]
    invoice_total_amount = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("invoice amount", True))
    ]
    salary_id = Annotated[UUID, BeforeValidator(is_uuid_validator("salary id"))]
    salary_company = Annotated[
        str | None, AfterValidator(is_string_validator("salary company", 2, 64, True))
    ]
    salary_occupation = Annotated[
        str | None, AfterValidator(is_string_validator("salary occupation", 2, 64, True))
    ]
    salary_salary = Annotated[
        Decimal | None, AfterValidator(is_decimal_validator("salary", True))
    ]
    salary_start_date = Annotated[date, BeforeValidator(is_date_validator("salary start_date"))]
    salary_end_date = Annotated[date, BeforeValidator(is_date_validator("salary end_date"))]


@dataclass
class GetValidator:
    limit = Annotated[int, AfterValidator(is_integer_validator("limit"))]
    offset = Annotated[int, AfterValidator(is_integer_validator("offset"))]
