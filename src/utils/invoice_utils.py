from graphql import GraphQLError
from src.utils.invoice_enum import InvoiceStatus, InvoiceType


def is_invoice_status_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, InvoiceStatus):
        raise GraphQLError(message=f"{name} must be valid invoice status")


def is_invoice_type_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, InvoiceType):
        raise GraphQLError(message=f"{name} must be valid invoice type")
