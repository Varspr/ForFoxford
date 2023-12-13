from sqlalchemy import select


class EmployerService:

    def __init__(self, connection, orm_mode):
        self.connection = connection
        self.orm_mode = orm_mode

    async def inner_employer(self, data: dict):
        async with self.connection() as session:
            session.add(self.orm_mode(**data))
            await session.flush()
            await session.commit()

    async def get_employer(self, employer_login: str) -> dict:
        async with self.connection() as session:
            result = await session.execute(select(self.orm_mode).where(self.orm_mode.login == employer_login))

            stmt = result.scalars().one()
            return stmt
