import asyncio

import uvicorn
from fastapi import FastAPI

from database.base.base import Base
from database.base.engine import engine, async_session
from database.dependencys.employer_dependency import employer_injection

from database.models.clients_table import ClientTable
from database.models.employer_table import EmployerTable
from database.models.message_table import MessageTable
from database.models.tickets_table import TicketsTable
from database.routes.message_router import router

app = FastAPI()
app.include_router(router)


async def client_with_ticket() -> None:
    async with async_session() as session:
        session.add_all(
            [
                MessageTable(client_rl=[ClientTable(name="John",
                                                    telegram_id=1234567)],
                             ticket_rl=[TicketsTable(client=1, status="Открыт")], ticket=1, employer=1, client=1,
                             text="Hello Foxford")])
        await session.commit()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def runer() -> None:
    await init_models()
    await employer_injection().inner_employer({"id": 1,
                                               "name": "Igor",
                                               "login": "Foxford",
                                               "password": "givemejob)"})


if __name__ == '__main__':
    asyncio.run(runer())

    # asyncio.run(client_with_ticket())
    uvicorn.run(app, host="127.0.0.1", port=8080)
