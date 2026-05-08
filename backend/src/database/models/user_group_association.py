from sqlalchemy import (
    Column, Integer, ForeignKey, Table
)
from src.database import Base


user_group_association = Table(
    'user_group_membership',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('extended_users.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True),
)
