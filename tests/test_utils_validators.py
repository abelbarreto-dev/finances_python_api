from datetime import date, datetime
from decimal import Decimal
from uuid import uuid4

import pytest
from sqlalchemy.inspection import inspect

from src.entities.entities import Bank, User
from src.inputs.MoneyLogInput import MoneyLogInputCreate
from src.inputs.PixInput import PixInputCreate
from src.utils.boolean_utils import is_boolean_validator
from src.utils.date_utils import is_date_validator
from src.utils.datetime_utils import is_datetime_validator
from src.utils.decimal_utils import is_decimal_validator
from src.utils.integer_utils import is_integer_validator
from src.utils.money_enum import MoneyMethod, MoneyType
from src.utils.pix_enum import PixType
from src.utils.string_utils import is_string_validator
from src.utils.username_utils import is_username_validator
from src.utils.uuid_utils import is_uuid_validator


def test_is_date_validator_returns_date_instance():
    validator = is_date_validator("birth_date")
    sample = date(2024, 1, 2)

    assert validator(sample) is sample


def test_is_datetime_validator_returns_datetime_instance():
    validator = is_datetime_validator("created_at")
    sample = datetime(2024, 1, 2, 3, 4, 5)

    assert validator(sample) is sample


def test_is_uuid_validator_returns_uuid_instance():
    validator = is_uuid_validator("id")
    sample = uuid4()

    assert validator(sample) is sample


def test_is_string_validator_accepts_none_when_nullable():
    validator = is_string_validator("name", is_nullable=True)

    assert validator(None) is None


def test_is_username_validator_rejects_none_without_nullable():
    validator = is_username_validator()

    with pytest.raises(Exception):
        validator(None)


def test_is_integer_validator_rejects_non_integer_values():
    validator = is_integer_validator("age")

    with pytest.raises(Exception):
        validator("10")


def test_is_decimal_validator_rejects_non_decimal_values():
    validator = is_decimal_validator("amount")

    with pytest.raises(Exception):
        validator("10.5")


def test_is_boolean_validator_rejects_non_boolean_values():
    validator = is_boolean_validator("active")

    with pytest.raises(Exception):
        validator("true")


def test_money_log_input_accepts_valid_money_method_and_type():
    model = MoneyLogInputCreate(
        user_id=uuid4(),
        type_opp=MoneyType.RECEIPT,
        method_opp=MoneyMethod.PIX,
        amount=Decimal("10.50"),
    )

    assert model.method_opp is MoneyMethod.PIX
    assert model.type_opp is MoneyType.RECEIPT


def test_pix_input_accepts_valid_pix_type():
    model = PixInputCreate(
        bank_id=uuid4(), name="Minha chave", pix_type=PixType.CPF, is_mine=True
    )

    assert model.pix_type is PixType.CPF


def test_user_entity_exposes_money_logs_relationship():
    relationships = {relationship.key for relationship in inspect(User).relationships}

    assert "money_logs" in relationships


def test_bank_entity_exposes_pixes_relationship():
    relationships = {relationship.key for relationship in inspect(Bank).relationships}

    assert "pixes" in relationships
