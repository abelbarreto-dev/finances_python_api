from graphql import GraphQLError
from src.utils.pix_enum import PixType


def is_pix_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, PixType):
        raise GraphQLError(message=f"{name} must be valid pix")
