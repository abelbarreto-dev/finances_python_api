from datetime import date
from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException

from src.utils.gender_enum import GenderType


def is_gender_validator(name: str, nullable: bool = False) -> Callable[[any | None], date]:
    def validator(value: any | None) -> date:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, GenderType):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid gender")
            )

        return date(value)

    return validator
