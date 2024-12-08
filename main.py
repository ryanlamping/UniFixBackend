# file that runs backend

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.database import *  # Ensure the import path is correct
from db.database import database
from fastapi.middleware.cors import CORSMiddleware
from api.auth import auth
from api.services import service
from api.contractors import contractor
from api.categories import category

# requiring database for application to connect
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(service.router, prefix="/services", tags=["services"])
app.include_router(contractor.router, prefix="/contractors", tags=["contractors"])
app.include_router(category.router, prefix="/category", tags=["category"])


# allowing CORS -- do we need?
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update to frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}