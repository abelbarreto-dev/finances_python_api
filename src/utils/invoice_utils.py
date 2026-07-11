from http.client import BAD_REQUEST

from fastapi import HTTPException

from src.utils.invoice_enum import InvoiceStatus, InvoiceType


def is_invoice_status_validator(name: str, value: any | None, nullable: bool = False) -> None:
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


def is_invoice_type_validator(name: str, value: any | None, nullable: bool = False) -> None:
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
