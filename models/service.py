from sqlalchemy import Column, String, Integer
from db.database import Base

class Service(Base):
    __tablename__ = "services"
    serviceid = Column(Integer, primary_key=True, autoincrement=True)
    typeid = Column(Integer)
    service = Column(String(100))
    rate = Column(String(100))