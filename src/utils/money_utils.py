from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException

from src.utils.money_enum import MoneyMethod, MoneyType


def is_money_type_validator(
    name: str, nullable: bool = False
) -> Callable[[any | None], MoneyType | None]:
    def validator(value: any | None) -> MoneyType | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, MoneyType):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid money type")
            )

        return value

    return validator


def is_money_method_validator(
    name: str, nullable: bool = False
) -> Callable[[any | None], MoneyMethod | None]:
    def validator(value: any | None) -> MoneyMethod | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, MoneyMethod):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid money method")
            )

        return value

    return validator
