from fastapi import APIRouter
from requests import Session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from sqlalchemy import select, distinct
from models.contractor import Contractor



router = APIRouter()

# get list of individual service names
# def contractorByService(db: Session):

def getAllContractors(db: Session):
    distinct_contractors = db.query(distinct(Contractor.contractorid)).all()
    return [contractor[0] for contractor in distinct_contractors]

# get a list of all contractors
@router.get("/distinct-contractors/")
def get_contractors(db: Session = Depends(get_db)):
    contractors = getAllContractors(db)
    return {"distinct_contractors": contractors}

# get contractor by type
def contractorsByType(db: Session, type: int):
    contractors = db.query(Contractor).filter(Contractor.typeid == type).all()
    return [contractor.contractorid for contractor in contractors]

@router.get("/contractor-by-type")
def contractor_by_type(type: int, db: Session = Depends(get_db)):
    contractors = contractorsByType(db, type)
    return contractors

def contractor_by_id(db: Session, id: int):
    contractors = db.query(Contractor).filter(Contractor.contractorid == id).first()
    return contractors

@router.get("/contractors-by-id/")
def get_contractor_by_id(id: int, db: Session = Depends(get_db)):
    contractors = contractor_by_id(db, id)
    return contractors
    