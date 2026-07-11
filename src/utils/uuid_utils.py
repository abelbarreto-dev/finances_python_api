from http.client import BAD_REQUEST
from uuid import UUID

from fastapi import HTTPException


def is_uuid_validator(name: str, value: any | None, nullable: bool = False) -> None:
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
