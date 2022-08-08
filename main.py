from sys import prefix
from fastapi import FastAPI
from routes.v1.v1_router import v1_router

from core.config import settings
from db.session import engine   #new
from db.base import Base  #new


app = FastAPI()

print("Create tables")
Base.metadata.create_all(bind=engine)

app.include_router(v1_router, prefix='/api/v1')