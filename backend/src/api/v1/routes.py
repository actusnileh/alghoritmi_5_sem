from fastapi import APIRouter

from src.api.v1.endpoints.lab1 import router as lab1


routers = APIRouter()
router_list = [
    lab1,
]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
