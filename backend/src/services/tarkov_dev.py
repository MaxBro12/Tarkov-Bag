from core.requests_makers import HttpMakerAsync

from src.settings import settings


class TarkovDevService(HttpMakerAsync):
    """
    Базовый сервис блокировки IP-адресов. Используется только для тестов.
    """

    def __init__(self):
        super().__init__(
            base_url=settings.TARKOV_DEV_URL,
            parse_method=self._get_simple_response,
        )

    async def items(self) -> tuple[dict, ...]:
        try:
            items = await self.post(json={'query': """
            {
                items(lang: ru) {
                    id
                    name
                }
            }
            """})
            return tuple(items.json['data']['items'])
        except KeyError as e:
            print(e)
            return tuple()


tarkov_dev_service = TarkovDevService()
