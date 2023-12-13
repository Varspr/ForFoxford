from typing import List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base.base import Base
from database.models.tickets_table import TicketsTable


class ClientTable(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    telegram_id: Mapped[str] = mapped_column(String, unique=True)
    tickets: Mapped[List[TicketsTable]] = relationship()

    # "TicketsTable", back_populates = "clients"

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.telegram_id}, {self.tickets}"

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "telegram_id": self.telegram_id,
                "ticket": [self.tickets]}
