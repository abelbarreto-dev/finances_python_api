from re import compile


def is_username(value: str) -> bool:
    regex = compile(r"^[a-z_][a-z_0-9]{2,63}$")

    checker = regex.match(value) is not None

    return checker
