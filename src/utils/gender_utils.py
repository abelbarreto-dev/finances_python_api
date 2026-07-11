from graphql import GraphQLError
from src.utils.gender_enum import GenderType


def is_gender_validator(value: any | None, name: str, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, GenderType):
        raise GraphQLError(message=f"{name} must be valid gender")
