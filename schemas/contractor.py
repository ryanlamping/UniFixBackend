from pydantic import BaseModel, EmailStr
from datetime import date

class ContractorCreate(BaseModel):
    password: str
    biography: str
    roleid: int
    typeid: int
    hoursid: int
    rating: str
    phonenumber: str
    
class Contractor(BaseModel):
    biography: str
    roleid: int
    addressid: int
    rating: str
    phonenumber: str