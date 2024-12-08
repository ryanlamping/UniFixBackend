from pydantic import BaseModel, EmailStr
from datetime import date

class Type(BaseModel):
    typeid: int
    type: str