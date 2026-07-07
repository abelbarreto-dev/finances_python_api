from http.client import BAD_REQUEST
from re import compile
from typing import Callable

from fastapi import HTTPException


def is_phone_validator(nullable: bool = False) -> Callable[[str | None], str | None]:
    def validator(value: str | None) -> str | None:
        if value is None and nullable:
            return value
        elif value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="phone cannot be nullable")
            )
        elif not isinstance(value, str):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="phone must be valid")
            )

        regex = compile(r"^\+[0-9]{12,13}$")

        checker = regex.match(value) is not None

        if not checker:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="phone must be valid")
            )

        return value

    return validator
