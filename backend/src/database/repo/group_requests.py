from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from core.sql_repository import RepositoryObj, ItemNotFound
from src.database.models.group_requests import GroupRequest


class GroupRequestRepo(RepositoryObj):
    def __init__(self, session: AsyncSession):
        super().__init__(GroupRequest, session=session, relationships=('user', 'group'))

    async def by_user_id(self, user_id: int, load_relations: bool = True) -> tuple[GroupRequest, ...]:
        return await self.some(
            filter_=GroupRequest.user_id == user_id,
            load_relations=load_relations,
        )

    async def by_user_group_id(
        self,
        user_id: int,
        group_id: int,
        load_relations: bool = True,
    ) -> GroupRequest | None:
        return await self.get(
            filter_=and_(GroupRequest.user_id == user_id, GroupRequest.group_id == group_id),
            load_relations=load_relations,
        )

    async def del_by_user_group_id(self, user_id: int, group_id: int) -> bool:
        request = await self.by_user_group_id(user_id=user_id, group_id=group_id, load_relations=False)
        if request is None:
            raise ItemNotFound(GroupRequest, 'user_id', user_id)
        return await self.delete(request)
