from pydantic import BaseModel, EmailStr
from datetime import date

class Tasks(BaseModel):
    type: str
    serviceid: int
    service: str