from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException

from src.utils.pix_enum import PixType


def is_pix_validator(name: str, nullable: bool = False) -> Callable[[any | None], PixType | None]:
    def validator(value: any | None) -> PixType | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, PixType):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid pix")
            )

        return value

    return validator
