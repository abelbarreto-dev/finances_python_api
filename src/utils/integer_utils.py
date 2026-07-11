from graphql import GraphQLError


def is_integer_validator(
    name: str, value: int | None, nullable: bool = False, negative: bool = False
) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} integer cannot be nullable")
    elif not isinstance(value, int) or isinstance(value, bool):
        raise GraphQLError(message=f"{name} must be an integer")
    elif not negative and value < 0:
        raise GraphQLError(message=f"{name} integer cannot be negative")
