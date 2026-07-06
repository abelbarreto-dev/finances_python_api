from re import compile
from typing import Callable


def is_phone_validator(nullable: bool = False) -> Callable[[str], str]:
    def validator(value: str) -> str:
        if value is None and nullable:
            return value

        regex = compile(r"^\+[0-9]{12,13}$")

        checker = regex.match(value) is not None

        if not checker:
            raise ValueError("phone must be valid")

        return value

    return validator
