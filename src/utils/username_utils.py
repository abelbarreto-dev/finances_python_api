from re import compile

from graphql import GraphQLError


def is_username_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="username cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="username must be valid")

    regex = compile(r"^[a-z_][a-z_0-9]{2,63}$")

    checker = regex.match(value) is not None

    if not checker:
        raise GraphQLError(message="username must be valid")
