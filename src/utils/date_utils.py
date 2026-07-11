from datetime import date, datetime
from http.client import BAD_REQUEST

from fastapi import HTTPException


def is_date_validator(value: any | None, name: str, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
        )
    elif not isinstance(value, date) or isinstance(value, datetime):
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid date")
        )
