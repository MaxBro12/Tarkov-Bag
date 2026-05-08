from sqlalchemy.ext.asyncio import AsyncSession

from core.sql_repository import RepositoryObj
from src.database.models.group import Group


class GroupRepo(RepositoryObj):
    def __init__(self, session: AsyncSession):
        super().__init__(Group, session=session)

    async def by_id(self, group_id: int, load_relations: bool = True) -> Group | None:
        return await self.get(
            filter_=Group.id == group_id,
            load_relations=load_relations,
        )
