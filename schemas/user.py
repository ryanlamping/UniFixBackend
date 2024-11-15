from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    roleid: int
    addressid: int
    phonenumber: str

class User(BaseModel):
    name: str
    email: EmailStr
    roleid: int
    addressid: int
    phonenumber: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    sub: str | None = None
    name: str | None = None
    email: str | None = None
    phonenumber: str | None = None