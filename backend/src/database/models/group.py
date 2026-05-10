from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .user_group_association import user_group_association
from src.database import Base


class Group(Base):
    """Группа пользователей"""
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey('extended_users.id'))

    owner: Mapped['ExtendedUser'] = relationship('ExtendedUser')

    members = relationship(
        "ExtendedUser",
        secondary=user_group_association,
        back_populates="member_of_groups",
        lazy="dynamic"
    )

    def __repr__(self):
        return f"<UserGroup(id={self.id})>"
