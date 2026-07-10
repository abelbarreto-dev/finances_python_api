from typing import Annotated
from uuid import UUID

from src.core.graphql import Arg, mutation
from src.dtos import MessageDTO, UserDTO
from src.inputs.UserInput import UserInputCreate, UserInputLogin


@mutation
async def login_user(user: Annotated[UserInputLogin, Arg()]) -> UserDTO:
    pass


@mutation
async def create_user(user: Annotated[UserInputCreate, Arg()]) -> UserDTO:
    pass


@mutation
async def update_user(user: Annotated[UserInputCreate, Arg()]) -> UserDTO:
    pass


@mutation
async def delete_user(id: Annotated[UUID, Arg()]) -> MessageDTO:
    pass
