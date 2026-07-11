from random import choice
from re import compile

from graphql import GraphQLError


def gen_valid_cnpj(is_alpha: bool = False):
    values: tuple[str] = tuple(dict_values(None).keys())

    if not is_alpha:
        values = tuple(i for i in values if i.isnumeric())

    cnpj = "".join(choice(values) for i in range(12))
    digit = calc_cnpj(cnpj, False)
    cnpj += digit
    digit = calc_cnpj(cnpj, True)

    return cnpj + digit


def is_cnpj_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise GraphQLError(message="cnpj cannot be nullable")
    elif not isinstance(value, str):
        raise GraphQLError(message="cnpj not matches")

    regex = compile(r"^[0-9A-Z]{14}$")

    if regex.match(value) is None:
        raise GraphQLError(message="cnpj not matches")

    checker = validate_cnpj(value)

    if not checker:
        raise GraphQLError(message="cnpj must be valid")


def validate_cnpj(value: str) -> bool:
    cnpj = value[0:12]

    digit = calc_cnpj(cnpj, False)

    cnpj += digit

    digit = calc_cnpj(cnpj, True)

    cnpj += digit

    return cnpj == value


def calc_cnpj(value: str, last: bool) -> str:
    weight = weights(last)

    sum_cnpj = 0
    id_weigth = 0

    for dg in value:
        sum_cnpj += dict_values(dg) * weight[id_weigth]
        id_weigth += 1

    eleven_mod = sum_cnpj % 11

    return str(0 if eleven_mod < 2 else 11 - eleven_mod)


def weights(last: bool) -> tuple[int]:
    weight = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

    if last:
        weight = (6, *weight)

    return weight


def dict_values(value: str | None) -> int | dict[str, int]:
    values = {}

    for val in range(10):
        key = str(val)
        values[key] = val

    for val in range(65, 91):
        key = chr(val)
        values[key] = val - 48

    return values[value] if value is not None else values
