import asyncio

from database.base.engine import async_session
from database.models.message_table import MessageTable
from database.service.messages_service import MessageService


def message_injection():
    return MessageService(async_session, MessageTable)

