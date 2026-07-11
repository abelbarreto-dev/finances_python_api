from graphql import GraphQLError


def is_boolean_validator(name: str, value: bool | None, nullable: bool = False) -> None:
    if nullable and value is None:
        return value
    elif not nullable and value is None:
        raise GraphQLError(message=f"{name} boolean cannot be nullable")
    elif not isinstance(value, bool):
        raise GraphQLError(message=f"{name} must be a boolean")
