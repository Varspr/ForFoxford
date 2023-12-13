from pydantic import BaseModel


class EmployerResponse(BaseModel):
    name: str
    login: str
