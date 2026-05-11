import json
import os
from src.database import DataBase
from src.depends.auth import ExtendedUserData
from src.settings import settings
from fastapi import HTTPException, status


class GroupHandler:
    def __init__(self, db: DataBase):
        self.db = db

    async def nicks(self, user_id: int) -> dict:
        """
        Возвращает список игровых ников пользователей кроме текущего.
        """
        return {'nicks': await self.db.users.nicks(user_id)}

    async def user_requests(self, user: ExtendedUserData):
        group_requests = await self.db.group_requests.by_user_id(user.id)

    async def approve(self, user: ExtendedUserData, group_id: int) -> dict:
        if user.extended is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not extended'
            )
        if await self.db.group_requests.del_by_user_group_id(user_id=user.id, group_id=group_id):
            user.extended.member_of_groups.append(group_id)
            return {'ok': True}
        return {'ok': False}

    async def reject(self, user: ExtendedUserData, group_id: int) -> dict:
        if user.extended is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not extended'
            )
        if await self.db.group_requests.del_by_user_group_id(user_id=user.id, group_id=group_id):
            return {'ok': True}
        return {'ok': False}

    async def leave(self, user: ExtendedUserData, group_id: int) -> dict:
        if user.extended is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not extended'
            )
        if group_id in user.extended.member_of_groups:
            user.extended.member_of_groups.remove(group_id)
            return {'ok': True}
        return {'ok': False}

    async def drop_user(self, user: ExtendedUserData, group_id: int, extended_user_id: int) -> dict:
        if user.extended is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not extended'
            )
        # TODO: добавь проверку что удаляет администратор группы
        if extended_user_id in user.extended.member_of_groups:
            user.extended.member_of_groups.remove(extended_user_id)
            return {'ok': True}
        return {'ok': False}

    async def user_groups(self, user: ExtendedUserData) -> dict:
        if user.extended is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User not extended'
            )
        groups = []
        for group in user.extended.member_of_groups:
            group = await self.db.groups.by_id(group.id)
            if group is None:
                continue
            members = []
            for member in group.members:
                if member.id == user.extended.id:
                    continue
                items = []
                for item in await self.db.user_items.by_user_id(member.id):
                    items.append({
                        'id': item.item_id,
                        'name': item.item.name,
                        'count': item.count
                    })
                members.append({
                    'nick': member.nick,
                    'items': items
                })
            groups.append({'id': group.id, 'members': members})
        print(groups)
        return {'groups': groups}
