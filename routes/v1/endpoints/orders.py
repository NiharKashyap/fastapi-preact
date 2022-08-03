from fastapi import APIRouter


orders_router = APIRouter()


@orders_router.get('/')
def root():
    return "Orders root api"