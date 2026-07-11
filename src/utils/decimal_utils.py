from decimal import Decimal

from graphql import GraphQLError


def is_decimal_validator(
    name: str, value: Decimal | None, nullable: bool = False, negative: bool = False
) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} decimal cannot be nullable")
    elif not isinstance(value, Decimal):
        raise GraphQLError(message=f"{name} must be a decimal")
    elif not negative and value < 0:
        raise GraphQLError(message=f"{name} decimal cannot be negative")
