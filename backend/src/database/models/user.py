from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer
from src.database import Base
from .user_group_association import user_group_association


class ExtendedUser(Base):
    __tablename__ = 'extended_users'

    id = mapped_column(Integer, primary_key=True)
    nick: Mapped[str] = mapped_column(unique=True)

    member_of_groups: Mapped[list['Group']] = relationship('Group', secondary=user_group_association)
    items: Mapped[list['UserItem']] = relationship(back_populates='user')
    group_requests: Mapped[list['GroupRequest']] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f'<User {self.id} {self.nick}>'

    def __str__(self) -> str:
        return f'User {self.nick}'
