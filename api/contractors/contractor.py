from fastapi import APIRouter
from requests import Session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from sqlalchemy import select, distinct
from models.service import Service



router = APIRouter()

# get list of individual service names
# def contractorByService(db: Session):