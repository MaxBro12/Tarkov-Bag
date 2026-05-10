from fastapi import APIRouter, HTTPException, status

from core.pydantic_misc_models import Ok, Detail
from core.fast_decorators import cache, rate_limiter
from core.redis_client import RedisDep
from core.fast_depends import PaginationParams
from src.depends import CommonDep
from src.handlers.groups import GroupHandler
from .models import UserGroupsRequestsResponse
from src.settings import settings


groups_router_v1 = APIRouter(prefix='/v1/groups', tags=['groups'])


@groups_router_v1.get('/{user_id}/requests', response_model=UserGroupsRequestsResponse)
@cache(key='requests:all', expire=1*60)
@rate_limiter(max_requests=20, time_delta=10)
async def all_requests(common: CommonDep, redis: RedisDep):
    """
    Получение всех запросов на добавление.
    """
    pass
