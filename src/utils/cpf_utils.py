from http.client import BAD_REQUEST
from random import choice
from re import compile
from typing import Callable

from fastapi import HTTPException


def gen_valid_cpf() -> str:
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    cpf = "".join(choice(numbers) for _ in range(9))

    cpf += calc_cpf_checker(cpf)

    return cpf + calc_cpf_checker(cpf)


def is_cpf_validator(nullable: bool = False) -> Callable[[str | None], str | None]:
    def validator(value: str | None) -> str | None:
        if value is None and nullable:
            return value
        elif value is None:
            raise HTTPException(
                status_code=BAD_REQUEST, detail=dict(message="cpf cannot be nullable")
            )
        elif not isinstance(value, str):
            raise HTTPException(status_code=BAD_REQUEST, detail=dict(message="cpf not matches"))

        checker = is_cpf_numeric(value)

        cpf = value[0:9]

        if not checker:
            raise HTTPException(status_code=BAD_REQUEST, detail=dict(message="cpf not matches"))

        digit = calc_cpf_checker(cpf)

        cpf += digit

        digits = digit + calc_cpf_checker(cpf)

        checker = value[9:11] == digits

        if not checker:
            raise HTTPException(status_code=BAD_REQUEST, detail=dict(message="cpf must be valid"))

        return value

    return validator


def is_cpf_numeric(value: str) -> bool:
    regex = compile(r"^[0-9]{11}$")
    return isinstance(value, str) and regex.match(value) is not None


def calc_cpf_checker(value: str):
    len_value = len(value) + 1

    sum_nums = 0
    id_value = 0

    for i in range(len_value, 1, -1):
        num = value[id_value]
        sum_nums += i * int(num)
        id_value += 1

    eleven_mod = sum_nums % 11

    return str(0 if eleven_mod < 2 else 11 - eleven_mod)
