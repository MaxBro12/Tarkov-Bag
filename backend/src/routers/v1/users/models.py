from typing import List

from pydantic import BaseModel


class Nicks(BaseModel):
    nicks: List[str]


class NewUser(BaseModel):
    nick: str


class NewItem(BaseModel):
    id: str
    count: int


class UserItem(NewItem):
    name: str


class UserItemsResponse(BaseModel):
    items: List[UserItem]


class NewItemsRequest(BaseModel):
    items: List[NewItem]
