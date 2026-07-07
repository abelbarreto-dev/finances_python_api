from http.client import BAD_REQUEST
from typing import Callable
from uuid import UUID

from fastapi import HTTPException


def is_uuid_validator(name: str, nullable: bool = False) -> Callable[[any | None], UUID]:
    def validator(value: any | None) -> UUID | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, UUID):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid uuid")
            )

        return value

    return validator
