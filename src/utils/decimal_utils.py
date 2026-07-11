from decimal import Decimal
from http.client import BAD_REQUEST

from fastapi import HTTPException


def is_decimal_validator(
    name: str, value: Decimal | None, nullable: bool = False, negative: bool = False
) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} decimal cannot be nullable")
        )
    elif not isinstance(value, Decimal):
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} must be a decimal")
        )
    elif not negative and value < 0:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} decimal cannot be negative")
        )
