from datetime import date, datetime

from graphql import GraphQLError


def is_date_validator(value: any | None, name: str, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, date) or isinstance(value, datetime):
        raise GraphQLError(message=f"{name} must be valid date")
