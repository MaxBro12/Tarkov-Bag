from sqlalchemy.ext.asyncio import AsyncSession

from core.sql_repository import RepositoryObj, ItemNotFound
from src.database.models.user_item_association import UserItem


class UserItemRepo(RepositoryObj):
    def __init__(self, session: AsyncSession):
        super().__init__(UserItem, session=session, relationships=('user', 'item'))

    async def by_user_id(self, user_id: int, load_relations: bool = True) -> tuple[UserItem, ...]:
        return await self.some(
            UserItem.user_id == user_id,
            load_relations=load_relations
        )

    async def del_by_user_id(self, user_id: int) -> bool:
        items = await self.by_user_id(user_id)
        if len(items) == 0:
            return False
        for item in items:
            await self.delete(item)
        return True

    async def new(self, user_id: int, item_id: str, count: int = 1, commit: bool = False) -> bool:
        return await self.add(UserItem(
            user_id=user_id, item_id=item_id, count=count
        ), commit=commit)
