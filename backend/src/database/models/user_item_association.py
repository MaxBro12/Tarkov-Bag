from sqlalchemy import (
    Column, Integer, ForeignKey, Table
)
from src.database import Base


user_item_association = Table(
    'user_items',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('extended_users.id'), primary_key=True),
    Column('item_id', Integer, ForeignKey('items.id'), primary_key=True),
    Column('quantity', Integer, default=1),
)
