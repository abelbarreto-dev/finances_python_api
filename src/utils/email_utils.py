from http.client import BAD_REQUEST
from re import compile
from typing import Callable

from fastapi import HTTPException


def is_email_validator(nullable: bool = False) -> Callable[[str | None], str | None]:
    def validator(value: str | None) -> str | None:
        if value is None and nullable:
            return value
        elif value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="email cannot be nullable")
            )
        elif not isinstance(value, str):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="email must be valid")
            )

        regex = compile(r"^(?=.{1,255}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        checker = regex.match(value) is not None

        if not checker:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="email must be valid")
            )

        return value

    return validator
