from sqlalchemy import Column, String, Integer
from db.database import Base

class Type(Base):
    __tablename__ = "type"
    typeid = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100))