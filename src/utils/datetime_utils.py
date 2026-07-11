from datetime import datetime
from http.client import BAD_REQUEST

from fastapi import HTTPException


def is_datetime_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
        )
    elif not isinstance(value, datetime):
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid datetime")
        )
