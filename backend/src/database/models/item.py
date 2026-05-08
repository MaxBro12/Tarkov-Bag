from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]

    def __repr__(self) -> str:
        return f'<Item id={self.id} name={self.name}>'

    def __str__(self) -> str:
        return f'Item {self.name}'

    @property
    def icon(self) -> str:
        return f'https://assets.tarkov.dev/{self.id}-icon.webp'
