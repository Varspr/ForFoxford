import asyncio

from database.base.engine import async_session
from database.models.employer_table import EmployerTable
from database.service.eployer_service import EmployerService


def employer_injection():
    return EmployerService(async_session, EmployerTable)



