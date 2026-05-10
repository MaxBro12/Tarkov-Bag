from typing import List
from pydantic import BaseModel


class ItemResponse(BaseModel):
    id: str
    name: str


class MultipleItemsResponse(BaseModel):
    items: List[ItemResponse]


class SyncCode(BaseModel):
    code: str
