from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from core.trash import generate_trash_string
from core.sql_repository import RepositoryObj, ItemNotFound
from src.database.models.user import ExtendedUser


class ExtendedUserRepo(RepositoryObj):
    def __init__(self, session: AsyncSession):
        super().__init__(ExtendedUser, session=session, relationships=('items', 'member_of_groups'))

    async def exists(self, user_id: int) -> bool:
        return await self._exists(ExtendedUser.id == user_id)

    async def by_id(self, user_id: int, load_relations: bool = True) -> ExtendedUser | None:
        return await self.get(
            ExtendedUser.id == user_id,
            load_relations=load_relations
        )

    async def by_name(self, nick: str, load_relations: bool = True) -> ExtendedUser | None:
        return await self.get(
            ExtendedUser.nick == nick,
            load_relations=load_relations
        )

    async def nicks(self) -> tuple[str, ...]:
        return tuple((await self.session.execute(select(ExtendedUser.nick))).scalars().all())

    async def new(
        self,
        id: str,
        nick: int,
        commit: bool = False
    ) -> bool:
        return await self.add(ExtendedUser(
            id=id,
            nick=nick,
        ), commit=commit)

    async def del_by_id(
        self,
        user_id: int,
        commit: bool = False
    ) -> bool:
        user = await self.by_id(user_id=user_id)
        if user is None:
            raise ItemNotFound(ExtendedUser, 'id', user_id)
        return await self.delete(obj=user, commit=commit)

    async def pagination(self, skip: int, limit: int, load_relations: bool = False) -> tuple[ExtendedUser, ...]:
        return await super()._pagination(
            skip=skip,
            limit=limit,
            load_relations=load_relations,
            order_by_field='id'
        )
