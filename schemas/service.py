from pydantic import BaseModel, EmailStr
from datetime import date

class Service(BaseModel):
    service: str
    rate: str