from fastapi import APIRouter, HTTPException, status

from core.pydantic_misc_models import Ok, Detail
from core.fast_decorators import cache, rate_limiter
from core.redis_client import RedisDep
from core.fast_depends import PaginationParams
from src.depends import CommonDep
from src.handlers.items import ItemHandler
from src.settings import settings
from .models import (
    MultipleItemsResponse,
    SyncCode,
)


items_router_v1 = APIRouter(prefix='/v1/items', tags=['items'])


@items_router_v1.get('', response_model=MultipleItemsResponse)
@cache(key='items:all', expire=60*60)
@rate_limiter(max_requests=20, time_delta=10)
async def all_items(pagination: PaginationParams, common: CommonDep, redis: RedisDep):
    """
    Получение всех предметов.
    """
    return await ItemHandler(common.db).all(
        skip=pagination.skip,
        limit=pagination.limit
    )


@items_router_v1.post('/sync', response_model=Ok | Detail)
@rate_limiter(max_requests=10, time_delta=60)
async def sync_database(sync_code: SyncCode, common: CommonDep):
    """
    Обновление базы предметов
    """
    if sync_code.code == settings.APP_ACCESS_KEY:
        return await ItemHandler(common.db).sync()
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid sync code'
    )
