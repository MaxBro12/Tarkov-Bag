from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base


class GroupRequest(Base):
    __tablename__ = 'group_requests'

    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('extended_users.id'), primary_key=True)

    user: Mapped['ExtendedUser'] = relationship(back_populates='group_requests')
    group: Mapped['Group'] = relationship()
