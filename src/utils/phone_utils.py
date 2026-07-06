from re import compile


def is_phone(value: str) -> bool:
    regex = compile(r"^\+[0-9]{12,13}$")

    checker = regex.match(value) is not None

    return checker
