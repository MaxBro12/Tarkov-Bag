from typing import Annotated
from dataclasses import dataclass

from fastapi import Depends, Request, Response

from src.handlers.auth import auth_handler, User
from src.database.models import ExtendedUser
from .db import DBDep


@dataclass(frozen=True, slots=True)
class ExtendedUserData(User):
    extended: ExtendedUser | None


async def verify_token(request: Request, response: Response, db: DBDep) -> ExtendedUserData:
    user = await auth_handler.verify_token(request, response)
    db_user = await db.users.by_id(user.id, load_relations=True)

    return ExtendedUserData(
        id=user.id,
        name=user.name,
        extended=db_user or None,
    )


UserDep = Annotated[ExtendedUserData, Depends(verify_token)]
