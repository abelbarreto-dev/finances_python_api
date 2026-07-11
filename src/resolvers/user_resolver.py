from datetime import date
from typing import Annotated
from uuid import UUID, uuid4

from src.core.graphql import Arg, mutation
from src.dtos.MessageDTO import MessageDTO
from src.dtos.UserDTO import UserDTO
from src.inputs.UserInput import UserInputCreate


@mutation
async def create_user(user: Annotated[UserInputCreate, Arg()]) -> UserDTO:
    user = UserInputCreate(**user)
    return UserDTO(
        id=uuid4(),
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        date_born=user.date_born,
        gender=user.gender,
        cpf=user.cpf,
        phone=user.phone,
        created_at=date.today(),
    )


@mutation
async def update_user(user: Annotated[UserInputCreate, Arg()]) -> UserDTO:
    user = UserInputCreate(**user)
    return UserDTO(
        id=uuid4(),
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        date_born=user.date_born,
        gender=user.gender,
        cpf=user.cpf,
        phone=user.phone,
        created_at=date.today(),
    )


@mutation
async def delete_user(id: Annotated[UUID, Arg()]) -> MessageDTO:
    return MessageDTO(message=f"User {id} deleted")
