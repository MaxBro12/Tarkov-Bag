from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class UserItem(Base):
    __tablename__ = 'user_items'
    user_id: Mapped[int] = mapped_column(ForeignKey('extended_users.id'), primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'), primary_key=True)
    count: Mapped[int] = mapped_column(default=1)

    # Связи с основными моделями
    user: Mapped["ExtendedUser"] = relationship(back_populates="items")
    item: Mapped["Item"] = relationship()
