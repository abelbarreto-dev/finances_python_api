from re import compile

from graphql import GraphQLError


def is_email_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="email cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="email must be valid")

    regex = compile(r"^(?=.{1,255}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    checker = regex.match(value) is not None

    if not checker:
        raise GraphQLError(message="email must be valid")
