from fastapi import HTTPException, status

from src.depends.auth import ExtendedUserData
from src.database import DataBase


class UsersHandler:
    def __init__(self, db: DataBase):
        self.db = db

    async def new_user(self, nick: str, user_id: int) -> dict:
        """
        Расширяет модель пользователя сервиса авторизации, добавляя игровой ник.
        """
        await self.db.users.new(id=user_id, nick=nick)
        # Автоматически добавляем в базовую группу пока не сделаю api groups
        if not await self.db.groups.exists(1):
            await self.db.groups.new(1)
        await self.db.flush()
        user = await self.db.users.by_id(user_id)
        if user is not None:
            user.member_of_groups.append(await self.db.groups.by_id(1))
            await self.db.flush()
        return {'ok': True}

    async def items(self, user: ExtendedUserData) -> dict:
        """
        Возвращает список предметов пользователя.
        """
        if user.extended is not None:
            items = await self.db.user_items.by_user_id(user_id=user.extended.id)
            ans = []
            for item in items:
                ans.append({
                    'id': item.item_id,
                    'name': item.item.name,
                    'count': item.count
                })
            return {'items': ans}
        else:
            items = []
        return {'items': items}

    async def sync_items(self, user: ExtendedUserData, items: list[dict]) -> dict:
        if user.extended is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not authorized'
            )
        try:
            await self.db.user_items.del_by_user_id(user_id=user.id)
            await self.db.flush()
            for item in items:
                if await self.db.items.exists(item['id']):
                    await self.db.user_items.new(
                        user_id=user.id,
                        item_id=item['id'],
                        count=item['count'],
                        commit=False
                    )
                else:
                    raise ValueError(f'Item {item["id"]} not found')
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        return {'ok': True}
