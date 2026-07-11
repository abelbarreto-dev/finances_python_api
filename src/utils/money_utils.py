from http.client import BAD_REQUEST

from fastapi import HTTPException

from src.utils.money_enum import MoneyMethod, MoneyType


def is_money_type_validator(name: str, value: any | None, nullable: bool = False) -> None:
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


def is_money_method_validator(name: str, value: any | None, nullable: bool = False) -> None:
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
