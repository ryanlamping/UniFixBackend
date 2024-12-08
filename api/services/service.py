from fastapi import APIRouter
from requests import Session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from sqlalchemy import select, distinct, func

from models.service import Service
from models.type import Type
from models.task import Task
from schemas.typeService import ServicesResponse

router = APIRouter()

# get list of individual service names
def get_all_services(db: Session):
    distinct_services = db.query(distinct(Service.service)).all()
    return [service[0] for service in distinct_services]

@router.get("/distinct-services/")
def get_services(db: Session = Depends(get_db)):
    services = get_all_services(db)
    return {"distinct_services": services}

def getAllTypes(db: Session):
    types = db.query(distinct(Type.type)).all()
    return [t[0] for t in types]

@router.get("/types/")
def getTypes(db: Session = Depends(get_db)):
    types = getAllTypes(db)
    return {"types: ": types}

# get type through service id
def get_type_through_service(service: int, db: Session):
    type = db.query(Service.typeid).filter(Service.serviceid == service).first()
    return type[0] if type else None

@router.get("/type-by-service/")
def type_by_service(service: int, db: Session = Depends(get_db)):
    type = get_type_through_service(service, db)
    return {"type by service": type}

# get list of services by contractor type
def get_services_by_type(type: int, db: Session):
    services = db.query(Service).filter(Service.typeid == type).all()
    return services

# send through url key: type, value = 1
@router.get("/services-by-type/")
def services_by_type(type: int, db: Session = Depends(get_db)):
    services = get_services_by_type(type, db)
    return {"services by type": services}

def get_type_and_service(db: Session):
    data = db.execute(
            select(
            Task.type,
            func.array_agg(func.json_build_object('id', Task.serviceid, 'name', Task.service))
        )
        .group_by(Task.type)
    )
    
    result = {row[0]: row[1] for row in data.fetchall()}
    return result

@router.get("/type-services/", response_model=ServicesResponse)
def get_services_and_types(db: Session = Depends(get_db)):
    data = get_type_and_service(db)
    return {"data": data}

