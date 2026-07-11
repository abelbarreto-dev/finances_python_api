from http.client import BAD_REQUEST
from re import compile

from fastapi import HTTPException


def is_code_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="bank code cannot be nullable")
        )
    elif not isinstance(value, str):
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="bank code must be valid")
        )

    regex = compile(r"^[0-9]{3}$")

    checker = regex.match(value)

    if checker is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="bank code must be valid")
        )


def is_agency_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="agency cannot be nullable")
        )
    elif not isinstance(value, str):
        raise HTTPException(status_code=BAD_REQUEST, detail=dict(message="agency must be valid"))

    regex = compile(r"^[0-9]{4,5}$")

    if regex.match(value) is None:
        raise HTTPException(status_code=BAD_REQUEST, detail=dict(message="agency must be valid"))


def is_account_number_validator(value: str | None, nullable: bool = False) -> None:
    if value is None and nullable:
        return value
    elif value is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="account number cannot be nullable")
        )
    elif not isinstance(value, str):
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="account number must be valid")
        )

    regex = compile(r"^[0-9]{5,12}?[0-9xX]$")

    if regex.match(value) is None:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=dict(message="account number must be valid")
        )
