from datetime import datetime

from pydantic import BaseModel


class MessageResponse(BaseModel):
    ticket: int
    employer: int
    client: int
    text: str
    send_time: datetime
