from graphql import GraphQLError
from src.utils.money_enum import MoneyMethod, MoneyType


def is_money_type_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, MoneyType):
        raise GraphQLError(message=f"{name} must be valid money type")


def is_money_method_validator(name: str, value: any | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, MoneyMethod):
        raise GraphQLError(message=f"{name} must be valid money method")
