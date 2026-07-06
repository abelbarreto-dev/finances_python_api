from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException


def is_string_validator(
    name: str,
    min_len: int = 0,
    max_len: int = 255,
    is_nullable: bool = False,
) -> Callable[[str], str]:
    def validator(value: str | None) -> str:
        if is_nullable and value is None:
            return value

        len_value = len(value)

        if len_value < min_len:
            raise HTTPException(
                status_code=BAD_REQUEST,
                detail=dict(message=f"{name} length must be greater then or equals to {min_len}"),
            )

        if len_value > max_len:
            raise HTTPException(
                status_code=BAD_REQUEST,
                detail=dict(message=f"{name} length must be less than or equals to {max_len}"),
            )

        return value

    return validator
