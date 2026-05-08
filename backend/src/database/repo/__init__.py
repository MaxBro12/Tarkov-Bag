from sqlalchemy.ext.asyncio import AsyncSession

from .item import ItemRepo
from .user import ExtendedUserRepo
from .group import GroupRepo
from core.sql_repository import DataBaseRepo


class DataBase(DataBaseRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.users = ExtendedUserRepo(session=session)
        self.items = ItemRepo(session=session)
        self.groups = GroupRepo(session=session)


__all__ = (
    'DataBase',
)
