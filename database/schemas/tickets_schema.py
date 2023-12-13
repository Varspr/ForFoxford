from datetime import datetime

from pydantic import BaseModel


class TicketResponse(BaseModel):
    client: int
    status: str
    date_of_create: datetime
    date_of_update: datetime
