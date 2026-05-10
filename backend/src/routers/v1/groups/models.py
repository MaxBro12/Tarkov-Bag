from pydantic import BaseModel


class Group(BaseModel):
    id: int
    members : list[str]
    owner_name: str


class UserGroupsRequestsResponse(BaseModel):
    groups: list[Group]
