from datetime import datetime

from pydantic import BaseModel


class Nicks(BaseModel):
    nicks: List[str]


class NewUser(BaseModel):
    nick: str


class NewItem(BaseModel):
    id: str
    count: int


class NewItemsRequest(BaseModel):
    items: tuple[NewItem, ...]
