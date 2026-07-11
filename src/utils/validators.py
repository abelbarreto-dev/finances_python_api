from src.inputs.BankBoxInput import BankBoxInputCreate, BankBoxInputUpdate, ListBankBoxInput
from src.inputs.BankInput import BankInputCreate, BankInputUpdate, ListBankInput
from src.inputs.CashInput import CashInputCreate, CashInputUpdate, ListCashInput
from src.inputs.InvoiceInput import InvoiceInputCreate, InvoiceInputUpdate, ListInvoiceInput
from src.inputs.LoginHistoryInput import (
    ListLoginHistoryInput,
    LoginHistoryInputCreate,
    LoginHistoryInputUpdate,
)
from src.inputs.MoneyLogInput import ListMoneyLogInput, MoneyLogInputCreate, MoneyLogInputUpdate
from src.inputs.PixInput import ListPixInput, PixInputCreate, PixInputUpdate
from src.inputs.SalaryInput import ListSalaryInput, SalaryInputCreate, SalaryInputUpdate
from src.inputs.UserInput import UserInputCreate, UserInputLogin, UserInputUpdate
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
from src.utils.gender_utils import is_gender_validator
from src.utils.integer_utils import is_integer_validator
from src.utils.invoice_utils import is_invoice_status_validator, is_invoice_type_validator
from src.utils.money_utils import is_money_method_validator, is_money_type_validator
from src.utils.phone_utils import is_phone_validator
from src.utils.pix_utils import is_pix_validator
from src.utils.string_utils import is_string_validator
from src.utils.username_utils import is_username_validator
from src.utils.uuid_utils import is_uuid_validator


class CreateValidator:
    @classmethod
    def user_validator(cls, user: UserInputCreate):
        is_string_validator("user full_name", user.full_name, 2, 64)
        is_date_validator(user.date_born, "user date_born")
        is_gender_validator(user.gender, "user gender")
        is_cpf_validator(user.cpf)
        is_email_validator(user.email)
        is_username_validator(user.username)
        is_string_validator("user password", user.password, 8, 255)
        is_phone_validator(user.phone)

    @classmethod
    def cash_validator(cls, cash: CashInputCreate):
        is_string_validator("cash tag", cash.tag, 2, 32)
        is_string_validator("cash description", cash.description, 0, 128, True)
        is_decimal_validator("cash balance", cash.balance, negative=True)

    @classmethod
    def bank_validator(cls, bank: BankInputCreate):
        is_code_validator(bank.code)
        is_string_validator("bank name", bank.name, 2, 64)
        is_agency_validator(bank.agency)
        is_account_number_validator(bank.account_number)
        is_decimal_validator("bank balance", bank.balance, negative=True)

    @classmethod
    def BankBoxValidator(cls, bank_box: BankBoxInputCreate):
        is_string_validator("bank box tag", bank_box.tag, 2, 32)
        is_string_validator("bank box description", bank_box.description, 0, 128, True)
        is_decimal_validator("bank box balance", bank_box.balance, negative=True)

    @classmethod
    def login_history_validator(cls, login_history: LoginHistoryInputCreate):
        is_datetime_validator("login history login time", login_history.login_time)

    @classmethod
    def money_log_validator(cls, money_log: MoneyLogInputCreate):
        is_money_type_validator("money log type enum", money_log.type_opp)
        is_money_method_validator("money log method enum", money_log.method_opp)
        is_decimal_validator("money amount", money_log.amount, negative=True)

    @classmethod
    def pix_validator(cls, pix: PixInputCreate):
        is_string_validator("pix name", pix.name, 2, 32)
        is_string_validator("pix description", pix.description, 0, 128, True)
        is_boolean_validator("pix is_mine", pix.is_mine)
        is_pix_validator("pix pix type", pix.pix_type)

    @classmethod
    def invoice_validator(cls, invoice: InvoiceInputCreate):
        is_string_validator("invoice name", invoice.name, 2, 32)
        is_string_validator("invoice description", invoice.description, 0, 255, True)
        is_date_validator(invoice.due_date, "invoice due_date")
        is_integer_validator("invoice installment", invoice.installments)
        is_integer_validator("invoice installs paid", invoice.installs_paid)
        is_decimal_validator("invoice amount", invoice.amount, negative=True)
        is_decimal_validator("invoice amount", invoice.total_amount, True, True)
        is_invoice_status_validator("invoice status", invoice.status)
        is_invoice_type_validator("invoice type", invoice.invoice_type)

    @classmethod
    def salary_validator(cls, salary: SalaryInputCreate):
        is_string_validator("salary company", salary.company, 2, 64, True)
        is_string_validator("salary occupation", salary.occupation, 2, 64, True)
        is_decimal_validator("salary", salary.salary, True)


class UpdateValidator:
    @classmethod
    def user_validator(user: UserInputUpdate):
        is_uuid_validator("user id", user.id)
        is_string_validator("user full_name", user.full_name, 2, 64, True)
        is_date_validator(user.date_born, "user date_born", True)
        is_gender_validator(user.gender, "user gender", True)
        is_cpf_validator(user.cpf, True)
        is_email_validator(user.email, True)
        is_username_validator(user.username, True)
        is_phone_validator(user.phone, True)

    @classmethod
    def cash_validator(cls, cash: CashInputUpdate):
        is_uuid_validator("cash id", cash.id)
        is_string_validator("cash tag", cash.tag, 2, 32, True)
        is_string_validator("cash description", cash.description, 0, 128, True)
        is_decimal_validator("cash balance", cash.balance, True, True)

    @classmethod
    def bank_validator(cls, bank: BankInputUpdate):
        is_uuid_validator("bank id", bank.id)
        is_code_validator(bank.code, True)
        is_string_validator("bank name", bank.name, 2, 64, True)
        is_agency_validator(bank.agency, True)
        is_account_number_validator(bank.account_number, True)
        is_decimal_validator("bank balance", bank.balance, True, True)

    @classmethod
    def bank_box_validator(bank_box: BankBoxInputUpdate):
        is_uuid_validator("bank box id", bank_box.id)
        is_string_validator("bank box tag", bank_box.tag, 2, 32, True)
        is_string_validator("bank box description", bank_box.description, 0, 128, True)
        is_decimal_validator("bank box balance", bank_box.balance, True, True)

    @classmethod
    def login_history_validator(cls, login_history: LoginHistoryInputUpdate):
        is_uuid_validator("login history id", login_history.id)
        is_datetime_validator("login history logout time", login_history.logout_time, True)

    @classmethod
    def money_log_validator(cls, money_log: MoneyLogInputUpdate):
        is_uuid_validator("money log id", money_log.id)
        is_money_type_validator("money log type enum", money_log.type_opp, True)
        is_money_method_validator("money log method enum", money_log.method_opp, True)
        is_decimal_validator("money amount", money_log.amount, True, True)

    @classmethod
    def pix_validator(cls, pix: PixInputUpdate):
        is_uuid_validator("pix id", pix.id)
        is_string_validator("pix name", pix.name, 2, 32, True)
        is_string_validator("pix description", pix.description, 0, 128, True)
        is_boolean_validator("pix is_mine", pix.is_mine, True)
        is_pix_validator("pix pix type", pix.pix_type, True)

    @classmethod
    def invoice_validator(cls, invoice: InvoiceInputUpdate):
        is_uuid_validator("invoice id", invoice.id)
        is_string_validator("invoice name", invoice.name, 2, 32, True)
        is_string_validator("invoice description", invoice.description, 0, 255, True)
        is_date_validator(invoice.due_date, "invoice due_date", True)
        is_integer_validator("invoice installments", invoice.installments, True)
        is_integer_validator("invoice installs paid", invoice.installs_paid, True)
        is_invoice_status_validator("invoice status", invoice.status, True)
        is_invoice_type_validator("invoice type", invoice.invoice_type, True)
        is_decimal_validator("invoice amount", invoice.amount, True, True)
        is_decimal_validator("invoice amount", invoice.total_amount, True, True)

    @classmethod
    def salary_validator(cls, salary: SalaryInputUpdate):
        is_uuid_validator("salary id", salary.id)
        is_string_validator("salary company", salary.company, 2, 64, True)
        is_string_validator("salary occupation", salary.occupation, 2, 64, True)
        is_decimal_validator("salary", salary.salary, True)


class AccessValidator:
    @classmethod
    def user_login_validator(login: UserInputLogin):
        is_username_validator(login.username)
        is_string_validator("user password", login.password, 8, 255)


class GetValidator:
    @classmethod
    def list_cash_validator(cls, cash: ListCashInput):
        is_integer_validator("cash limit", cash.limit)
        is_integer_validator("cash offset", cash.offset)
        is_string_validator("cash tag", cash.tag, 2, 32, True)

    @classmethod
    def list_bank_validator(cls, bank: ListBankInput):
        is_integer_validator("bank box limit", bank.limit)
        is_integer_validator("bank box offset", bank.offset)
        is_string_validator("bank name", bank.name, 2, 64, True)
        is_string_validator("bank code", bank.code, 2, 64, True)

    @classmethod
    def list_bank_box_validator(bank_box: ListBankBoxInput):
        is_integer_validator("bank box limit", bank_box.limit)
        is_integer_validator("bank box offset", bank_box.offset)
        is_uuid_validator("bank box bank id", bank_box.bank_id)
        is_string_validator("bank box tag", bank_box.tag, 2, 32, True)

    @classmethod
    def list_login_history_validator(cls, login_history: ListLoginHistoryInput):
        is_integer_validator("login history limit", login_history.limit)
        is_integer_validator("login history offset", login_history.offset)
        is_date_validator(login_history.due_date, "login history due_date", True)

    @classmethod
    def list_money_log_validator(cls, money_log: ListMoneyLogInput):
        is_integer_validator("money log limit", money_log.limit)
        is_integer_validator("money log offset", money_log.offset)
        is_uuid_validator("money log bank id", money_log.bank_id, True)
        is_uuid_validator("money log bank box id", money_log.bank_box_id, True)
        is_uuid_validator("money log cash id", money_log.cash_id, True)
        is_uuid_validator("money log invoice id", money_log.invoice_id, True)
        is_money_type_validator("money log type enum", money_log.type_opp, True)
        is_money_method_validator("money log method enum", money_log.method_opp, True)

    @classmethod
    def list_pix_validator(cls, pix: ListPixInput):
        is_integer_validator("pix limit", pix.limit)
        is_integer_validator("pix offset", pix.offset)
        is_uuid_validator("pix bank id", pix.bank_id, True)
        is_string_validator("pix name", pix.name, 2, 32, True)
        is_pix_validator("pix pix type", pix.pix_type, True)
        is_boolean_validator("pix is_mine", pix.is_mine, True)

    @classmethod
    def list_invoice_validator(cls, invoice: ListInvoiceInput):
        is_integer_validator("invoice limit", invoice.limit)
        is_integer_validator("invoice offset", invoice.offset)
        is_string_validator("invoice name", invoice.name, 2, 32, True)
        is_integer_validator("invoice installments", invoice.installments, True)
        is_date_validator(invoice.due_date, "invoice due_date", True)
        is_invoice_type_validator("invoice type", invoice.invoice_type, True)
        is_invoice_status_validator("invoice status", invoice.status, True)

    @classmethod
    def list_salary_validator(cls, salary: ListSalaryInput):
        is_integer_validator("salary limit", salary.limit)
        is_integer_validator("salary offset", salary.offset)
        is_string_validator("salary company", salary.company, 2, 64, True)
        is_string_validator("salary occupation", salary.occupation, 2, 64, True)
        is_decimal_validator("salary", salary.salary, True)
