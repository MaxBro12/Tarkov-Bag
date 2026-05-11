from sqlalchemy.ext.asyncio import AsyncSession

from core.sql_repository import RepositoryObj
from src.database.models.group import Group


class GroupRepo(RepositoryObj):
    def __init__(self, session: AsyncSession):
        super().__init__(Group, session=session, relationships=('members',))

    async def exists(self, group_id: int) -> bool:
        return await self._exists(Group.id == group_id)

    async def by_id(self, group_id: int, load_relations: bool = True) -> Group | None:
        return await self.get(
            filter_=Group.id == group_id,
            load_relations=load_relations,
        )

    async def new(self, group_id: int, owner_id: int = 1) -> bool:
        return await self.add(Group(id=group_id, owner_id=owner_id))
