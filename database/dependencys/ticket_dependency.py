import asyncio

from database.base.engine import async_session
from database.models.tickets_table import TicketsTable
from database.service.tickets_service import TicketService


def ticket_injection():
    return TicketService(async_session, TicketsTable)

