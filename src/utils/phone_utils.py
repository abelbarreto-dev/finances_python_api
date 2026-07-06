from http.client import BAD_REQUEST
from re import compile
from typing import Callable

from fastapi import HTTPException


def is_phone_validator(nullable: bool = False) -> Callable[[str], str]:
    def validator(value: str) -> str:
        if value is None and nullable:
            return value

        regex = compile(r"^\+[0-9]{12,13}$")

        checker = regex.match(value) is not None

        if not checker:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="phone must be valid")
            )

        return value

    return validator
