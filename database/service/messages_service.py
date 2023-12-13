from sqlalchemy import select


class MessageService:

    def __init__(self, connection, orm_mode):
        self.connection = connection
        self.orm_mode = orm_mode

    async def inner_message(self, data: dict):
        async with self.connection() as session:
            session.add(self.orm_mode(**data))
            await session.flush()
            await session.commit()

    async def get_message(self, message_id: int) -> dict:
        async with self.connection() as session:
            result = await session.execute(select(self.orm_mode).where(self.orm_mode.id == message_id))

            stmt = result.scalars().one()
            return stmt
