

from sqlalchemy import select

from database.base.engine import async_session
from database.models.clients_table import ClientTable


class ClientService:

    def __init__(self, connection, orm_mode):
        self.connection = connection
        self.orm_mode = orm_mode

    async def inner_client(self, client: dict):
        async with self.connection() as session:
            session.add(self.orm_mode(**client))
            await session.flush()
            await session.commit()

    async def get_client(self, client: int) -> dict:
        async with self.connection() as session:
            result = await session.execute(select(self.orm_mode).where(self.orm_mode.id == client))

            stmt = result.scalars().one()
            return stmt



