from fastapi import APIRouter
from requests import Session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from sqlalchemy import select, distinct
from models.type import Type

router = APIRouter()

def getAllTypes(db: Session):
    types = db.query(distinct(Type.type)).all()
    return types

@router.get("/types/")
def getTypes(db: Session = Depends(get_db)):
    types = getAllTypes(db)
    return {"types: ": types}