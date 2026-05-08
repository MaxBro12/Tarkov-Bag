from fastapi import APIRouter, HTTPException

from core.pydantic_misc_models import Ok
from core.fast_decorators import cache, rate_limiter
from core.redis_client import RedisDep
from src.depends import CommonDep
from src.handlers.users import UsersHandler
from .models import Nicks, NewUser


users_router_v1 = APIRouter(prefix='/v1/users', tags=['users'])


@users_router_v1.get('/nicks', response_model=Nicks)
@cache(key='users:nicks', expire=5*60)
@rate_limiter(max_requests=10, time_delta=10)
async def all_nicks(common: CommonDep, redis: RedisDep):
    """
    Получаем список всех никнеймов пользователей.
    """
    return await UsersHandler(common.db).nicks()


@users_router_v1.post('/new', response_model=Ok)
@rate_limiter(max_requests=10, time_delta=30)
async def post_new_user(user: NewUser, common: CommonDep):
    """
    Создание нового пользователя. Вам потребуется:
        - 'nick' - никнейм пользователя
    """
    return await UsersHandler(common.db).new_user(nick=user.nick, user_id=common.user.id)
