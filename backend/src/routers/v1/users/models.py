from typing import List, Literal
from datetime import datetime

from pydantic import BaseModel


class Nicks(BaseModel):
    nicks: List[str]


class NewUser(BaseModel):
    nick: str
