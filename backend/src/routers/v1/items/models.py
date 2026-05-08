from typing import List
from pydantic import BaseModel


class ItemResponse(BaseModel):
    id: int
    name: str
    icon: str


class MultipleItemsResponse(BaseModel):
    items: List[ItemResponse]


class SyncCode(BaseModel):
    code: str
