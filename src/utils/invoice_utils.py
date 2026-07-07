from http.client import BAD_REQUEST
from typing import Callable

from fastapi import HTTPException

from src.utils.invoice_enum import InvoiceStatus, InvoiceType


def is_invoice_status_validator(
    name: str, nullable: bool = False
) -> Callable[[any | None], InvoiceStatus | None]:
    def validator(value: any | None) -> InvoiceStatus | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, InvoiceStatus):
            raise HTTPException(
                status_code=BAD_REQUEST,
                detail=dict(message=f"{name} must be valid invoice status"),
            )

        return value

    return validator


def is_invoice_type_validator(
    name: str, nullable: bool = False
) -> Callable[[any | None], InvoiceType | None]:
    def validator(value: any | None) -> InvoiceType | None:
        if nullable and value is None:
            return value
        elif not nullable and value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} cannot be nullable")
            )
        elif not isinstance(value, InvoiceType):
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message=f"{name} must be valid invoice type")
            )

        return value

    return validator
