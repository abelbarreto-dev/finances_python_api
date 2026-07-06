from http.client import BAD_REQUEST
from re import compile
from typing import Callable

from fastapi import HTTPException


def is_username_validator(nullable: bool = False) -> Callable[[str], str]:
    def validator(value: str) -> str:
        if value is None and nullable:
            return value

        regex = compile(r"^[a-z_][a-z_0-9]{2,63}$")

        checker = regex.match(value) is not None

        if not checker:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="username must be valid")
            )

        return value

    return validator
