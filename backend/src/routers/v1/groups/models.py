from pydantic import BaseModel


class Group(BaseModel):
    id: int
    members : list[str]
    owner_name: str


class UserGroupsRequestsResponse(BaseModel):
    groups: list[Group]


class Item(BaseModel):
    id: str
    name: str
    count: int


class OtherUsersItems(BaseModel):
    nick: str
    items: list[Item]


class GroupMembers(BaseModel):
    id: int
    members: list[OtherUsersItems]


class UserGroupsResponse(BaseModel):
    groups: list[GroupMembers]
