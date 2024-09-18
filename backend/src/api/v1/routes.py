from fastapi import APIRouter

from src.api.v1.endpoints.lab1 import router as lab1
from src.api.v1.endpoints.lab2 import router as lab2


routers = APIRouter()
router_list = [
    lab1,
    lab2,
]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
