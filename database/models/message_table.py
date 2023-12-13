from datetime import datetime
from typing import List

from sqlalchemy import Integer, String, ForeignKey, DateTime, func, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base.base import Base
from database.models.clients_table import ClientTable
from database.models.tickets_table import TicketsTable


class MessageTable(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    employer: Mapped[int] = mapped_column(Integer, ForeignKey("employers.id"))
    client: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id"))

    text: Mapped[Text] = mapped_column(Text)
    send_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    client_rl: Mapped[List[ClientTable]] = relationship()


    # "TicketsTable", back_populates = "messages"

    def __repr__(self):
        return (f"{self.id}, {self.ticket}, {self.employer}, {self.client}, {self.text}, {self.send_time},"
                f"{self.client_rl}, {self.ticket_rl}")

    def to_dict(self):
        return {"id": self.id,
                "ticket": self.ticket,
                "employer": self.employer,
                "client": self.client,
                "text": self.text,
                "send_time": self.send_time,
                "client_rl": {self.client_rl},
                "ticket_rl": {self.ticket_rl}}
