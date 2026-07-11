from re import compile

from graphql import GraphQLError


def is_phone_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="phone cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="phone must be valid")

    regex = compile(r"^\+[0-9]{12,13}$")

    checker = regex.match(value) is not None

    if not checker:
        raise GraphQLError(message="phone must be valid")
