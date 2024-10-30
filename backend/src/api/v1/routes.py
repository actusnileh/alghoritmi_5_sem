from fastapi import APIRouter

from src.api.v1.endpoints.lab1 import router as lab1
from src.api.v1.endpoints.lab2 import router as lab2
from src.api.v1.endpoints.lab3 import router as lab3
from src.api.v1.endpoints.lab4 import router as lab4
from src.api.v1.endpoints.lab5 import router as lab5
from src.api.v1.endpoints.lab6 import router as lab6


routers = APIRouter()
router_list = [
    lab1,
    lab2,
    lab3,
    lab4,
    lab5,
    lab6,
]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
