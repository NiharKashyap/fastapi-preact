from sys import prefix
from fastapi import FastAPI
from routes.v1.v1_router import v1_router

app = FastAPI()


app.include_router(v1_router, prefix='/api/v1')