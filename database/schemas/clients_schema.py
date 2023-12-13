from pydantic import BaseModel


class ClientsTableResponse(BaseModel):
    name: str
    telegram_id: int