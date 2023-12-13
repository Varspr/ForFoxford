from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from database.base.base import Base


class EmployerTable(Base):
    __tablename__ = "employers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    login: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.login}, {self.password}"

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "login": self.login,
                "password": self.password}
