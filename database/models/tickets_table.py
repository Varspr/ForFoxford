from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from database.base.base import Base


class TicketsTable(Base):
    __tablename__ = 'tickets'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, unique=True, primary_key=True)
    client: Mapped[int] = mapped_column(ForeignKey('clients.id'))
    status: Mapped[str] = mapped_column(String, default="Открыт")
    date_of_create: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    date_of_update: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # client_rl: Mapped[List[ClientTable]] = relationship("ClientTable", back_populates="tickets")
    # messages: Mapped[List[MessageTable]] = relationship("MessageTable", back_populates="tickets")

    def __repr__(self):
        return f"{self.id}, {self.client}, {self.status}, {self.date_of_create}, {self.date_of_update},"
# f"{self.client_rl}, {self.messages}")

    def to_dict(self):
        return {'id': self.id,
                "client": self.client,
                "status": self.status,
                "date_of_create": self.date_of_create,
                "date_of_update": self.date_of_update, }
        # "client_rl": [self.client_rl],
        # "messages": [self.messages]
