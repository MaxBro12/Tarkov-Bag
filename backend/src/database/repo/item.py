import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.sql_repository import RepositoryObj, ItemNotFound
from src.database.models.item import Item


class ItemRepo(RepositoryObj):
    def __init__(self, session: AsyncSession):
        super().__init__(Item, session=session)

    async def by_id(self, Item_id: int, load_relations: bool = True) -> Item | None:
        return await self.get(
            filter_=Item.id == Item_id,
            load_relations=load_relations,
        )

    async def by_name(self, name: str) -> Item | None:
        return await self.get(Item.name == name)

    async def new(
        self,
        id: str,
        name: str,
        commit: bool = False
    ) -> bool:
        try:
            return await self.add(Item(
                id=id,
                name=name,
            ), commit=commit)
        except IntegrityError:
            logging.error(f'Cant insert {name} exists')
            return False

    async def del_by_id(self, Item_id: int, commit: bool = False) -> bool:
        data = await self.by_id(Item_id)
        if data is None:
            raise ItemNotFound(Item, 'id', Item_id)
        return await self.delete(data, commit=commit)

    async def pagination(self, skip: int, limit: int, load_relations: bool = False) -> tuple[Item]:
        return await self._pagination(
            skip=skip,
            limit=limit,
            load_relations=load_relations,
            order_by_field='created_at',
        )
