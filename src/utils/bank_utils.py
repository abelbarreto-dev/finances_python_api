from re import compile

from graphql import GraphQLError


def is_code_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="bank code cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="bank code must be valid")

    regex = compile(r"^[0-9]{3}$")

    checker = regex.match(value)

    if checker is None:
        raise GraphQLError(message="bank code must be valid")


def is_agency_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="agency cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="agency must be valid")

    regex = compile(r"^[0-9]{4,5}$")

    if regex.match(value) is None:
        raise GraphQLError(message="agency must be valid")


def is_account_number_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="account number cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="account number must be valid")

    regex = compile(r"^[0-9]{5,12}?[0-9xX]$")

    if regex.match(value) is None:
        raise GraphQLError(message="account number must be valid")
