from datetime import datetime

from graphql import GraphQLError


def is_datetime_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, datetime):
        raise GraphQLError(message=f"{name} must be valid datetime")
