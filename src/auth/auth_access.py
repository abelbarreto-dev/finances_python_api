from datetime import date
from uuid import uuid4

from fastapi import Request

from src.dtos.UserDTO import UserDTO
from src.inputs.UserInput import UserInputLogin
from src.utils.gender_enum import GenderType
from src.utils.validators import AccessValidator


async def auth_login_user(request: Request) -> UserDTO:
    body = await request.json()
    user = UserInputLogin(**body)
    AccessValidator.user_login_validator(user)

    return UserDTO(
        id=uuid4(),
        full_name="Full Name",
        username=user.username,
        email="fullnameuser@service.com",
        date_born=date(2001, 4, 9),
        gender=GenderType.FEMALE,
        cpf="56582145578",
        phone=None,
        created_at=date(2026, 7, 9),
    )
