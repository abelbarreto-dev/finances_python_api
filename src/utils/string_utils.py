from graphql.error import GraphQLError


def is_string_validator(
    name: str,
    value: str | None,
    min_len: int = 0,
    max_len: int = 255,
    is_nullable: bool = False,
) -> None:
    if is_nullable and value is None:
        return value
    elif value is None:
        raise GraphQLError(message=f"{name} cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message=f"{name} must be a string")

    len_value = len(value)

    if len_value < min_len:
        raise GraphQLError(message=f"{name} length must be greater then or equals to {min_len}")

    if len_value > max_len:
        raise GraphQLError(message=f"{name} length must be less than or equals to {max_len}")
