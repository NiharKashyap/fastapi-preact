from fastapi import APIRouter



user_router = APIRouter()



@user_router.get("/", description="Root Users")
def root():
    return "Root API"