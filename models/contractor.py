from sqlalchemy import Column, String, Integer
from db.database import Base

class Contractor(Base):
    __tablename__ = "contractor"
    contractorid = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(255), nullable=False)
    biography = Column(String(255))
    roleid = Column(Integer)
    addressid = Column(Integer)
    typeid = Column(Integer)
    hoursid = Column(Integer)
    rating = Column(String(100))
    phonenumber = Column(String(15))