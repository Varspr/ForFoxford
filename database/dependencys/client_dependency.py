import asyncio
from http.client import HTTPException

from database.base.engine import async_session
from database.models.clients_table import ClientTable
from database.models.tickets_table import TicketsTable
from database.service.client_service import ClientService


def client_injection():
    return ClientService(async_session, ClientTable)

