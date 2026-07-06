from random import choice
from re import compile


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


def gen_valid_cpf() -> str:
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    cpf = "".join(choice(numbers) for _ in range(9))

    cpf += calc_cpf_checker(cpf)

    return cpf + calc_cpf_checker(cpf)


def gen_invalid_cpf() -> str:
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    cpf = "".join(choice(numbers) for _ in range(11))

    if is_cpf_validator(cpf):
        return gen_invalid_cpf()

    return cpf


def is_cpf_numeric(value: str) -> bool:
    regex = compile(r"^[0-9]{11}$")
    return regex.match(value) is not None


def is_cpf_validator(value: str) -> bool:
    checker = is_cpf_numeric(value)

    cpf = value[0:9]

    if not checker:
        return False

    digit = calc_cpf_checker(cpf)

    cpf += digit

    digits = digit + calc_cpf_checker(cpf)

    return value[9:11] == digits
