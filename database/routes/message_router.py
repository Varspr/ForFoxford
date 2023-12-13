from datetime import datetime

from fastapi import APIRouter, HTTPException

from database.base.engine import async_session
from database.dependencys.client_dependency import client_injection
from database.dependencys.message_dependency import message_injection
from database.dependencys.ticket_dependency import ticket_injection
from database.models.clients_table import ClientTable
from database.models.message_table import MessageTable
from database.models.tickets_table import TicketsTable

router = APIRouter(
    prefix="/message",
    tags=["message"],
    responses={404: {"description": "Not found"}},
)


@router.post("/client/{api_key}")
async def post_client(api_key: str,
                      client_name: str,
                      client_id: int,
                      client_tg_id: str,
                      ) -> None:
    if api_key != 'boba':
        raise HTTPException(status_code=401, detail=f"Wrong api key")
    await client_injection().inner_client({
        "id": client_id,
        "name": client_name,
        "telegram_id": client_tg_id, })


@router.post("/message/{message_id}")
async def post_message(client_id: int, employer_id: int,
                       text: str, client_name: str,
                       telegram_id: int, status: str) -> str:
    client = await client_injection().get_client(client_id)
    if client is None:
        raise HTTPException(status_code=404, detail=f"User not found")
    async with async_session() as session:
        session.add_all(
            [
                # Сложная и костылевая конструкция возникшая в связи с использованием новых инструментов и
                # прилетов багов от незнания новой операционки
                MessageTable(clients_rl=[ClientTable(name=client_name, telegram_id=telegram_id,
                                                     tickets=[TicketsTable(client=client_id, status=status)])],
                             employer=employer_id, client=client_id, text=text)])
        await session.commit()
