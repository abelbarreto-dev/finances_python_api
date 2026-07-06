from re import compile
from typing import Callable


def is_username_validator(nullable: bool = False) -> Callable[[str], str]:
    def validator(value: str) -> str:
        if value is None and nullable:
            return value

        regex = compile(r"^[a-z_][a-z_0-9]{2,63}$")

        checker = regex.match(value) is not None

        if not checker:
            raise ValueError("username must be valid")

        return value

    return validator
