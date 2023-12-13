from sqlalchemy import select
from database.base.engine import async_session


class TicketService:

    def __init__(self, connection, orm_mode):
        self.connection = connection
        self.orm_mode = orm_mode

    async def inner_ticket_(self, ticket: dict):
        async with self.connection() as session:
            session.add(self.orm_mode(**ticket))
            await session.flush()
            await session.commit()

    async def get_ticket_(self, сlient_id: int) -> dict:
        async with self.connection() as session:
            result = await session.execute(select(self.orm_mode).where(self.orm_mode.client == сlient_id))

            stmt = result.scalars().one()
            return stmt

    async def update_ticket(self, client_id: int, new_status):
        async with self.connection() as session:
            result = await session.execute(select(self.orm_mode).where(self.orm_mode.client == client_id))

            stmt = result.scalars().one()
            stmt.status = new_status
            await session.flush()
            await session.commit()

    async def ordering_by_status(self):
        async with self.connection() as session:

            result = await session.execute(select(self.orm_mode).order_by(self.orm_mode.status))

            stmt = result.scalars().all()

            for ticket in stmt:

                print(ticket.id, ticket.client, ticket.status, ticket.date_of_create, ticket.date_of_update)
