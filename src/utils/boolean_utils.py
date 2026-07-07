from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException


def is_boolean_validator(
    name: str, nullable: bool = False
) -> Callable[[bool | None], bool | None]:
    def validator(value: bool | None) -> bool | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} boolean cannot be nullable")
            )
        elif not isinstance(value, bool):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be a boolean")
            )

        return value

    return validator
