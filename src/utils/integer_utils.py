from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException


def is_integer_validator(
    name: str, nullable: bool = False, negative: bool = False
) -> Callable[[int | None], int | None]:
    def validator(value: int | None) -> int | None:
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

        return value

    return validator
