from sqlalchemy import Column, String, Integer
from db.database import Base

class Task(Base):
    __tablename__ = "tasks"
    type = Column(Integer, primary_key=True, autoincrement=True)
    serviceid = Column(Integer)
    service = Column(String(100))