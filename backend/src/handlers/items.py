import json
import os
from src.database import DataBase, Item
from src.services.tarkov_dev import tarkov_dev_service
from src.settings import settings


class ItemHandler:
    def __init__(self, db: DataBase):
        self.db = db

    @staticmethod
    async def _item_to_dict(item: Item) -> dict:
        return {
            'id': item.id,
            'name': item.name,
            'icon': item.icon
        }

    async def all(self, skip: int | None = 0, limit: int | None = 100) -> dict:
        """
        Возвращает список всех предметов.
        """
        items = await self.db.items.pagination(
            skip=skip or 0,
            limit=limit or 100,
            load_relations=True
        )
        return {'items': [self._item_to_dict(
            item,
        ) for item in items]}

    async def sync(self) -> dict:
        await self.db.items.clear_table()
        if settings.DEBUG:
            if not os.path.exists('items.json'):
                items = await tarkov_dev_service.items()
                with open('items.json', 'w') as f:
                    json.dump(items, f)
                return {'ok': False}

            with open('items.json') as f:
                items = json.load(f)
        else:
            items = await tarkov_dev_service.items()

        ids = []
        for item in items:
            if item['id'] not in ids:
                ids.append(item['id'])
                await self.db.items.add(Item(**item))
        return {'ok': True}
