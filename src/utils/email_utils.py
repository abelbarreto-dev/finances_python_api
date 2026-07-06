from re import compile


def is_email(value: str) -> bool:
    regex = compile(r"^(?=.{1,255}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    checker = regex.match(value) is not None

    return checker
