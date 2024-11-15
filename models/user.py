from sqlalchemy import Column, Date, Integer, String
from db.database import Base

# getting user metadata from postgresql database: 

class User(Base):
    __tablename__ = "users"
    userid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    roleid = Column(Integer)
    addressid = Column(Integer)
    phonenumber = Column(String(15))
