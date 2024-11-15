from fastapi import APIRouter
from requests import Session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from sqlalchemy import select, distinct
from models.service import Service



router = APIRouter()

# get list of individual service names
def getAllServices(db: Session):
    distinct_services = db.query(distinct(Service.service)).all()
    return [service[0] for service in distinct_services]

@router.get("/distinct-services/")
def get_services(db: Session = Depends(get_db)):
    services = getAllServices(db)
    return {"distinct_services": services}