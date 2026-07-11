from http.client import BAD_REQUEST

from fastapi import HTTPException


def is_integer_validator(
    name: str, value: int | None, nullable: bool = False, negative: bool = False
) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} integer cannot be nullable")
        )
    elif not isinstance(value, int) or isinstance(value, bool):
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} must be an integer")
        )
    elif not negative and value < 0:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message=f"{name} integer cannot be negative")
        )
