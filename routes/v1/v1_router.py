from fastapi import APIRouter

from routes.v1.endpoints.users import user_router
from routes.v1.endpoints.orders import orders_router


v1_router = APIRouter()


v1_router.include_router(user_router, prefix="/users")
v1_router.include_router(orders_router, prefix="/orders")