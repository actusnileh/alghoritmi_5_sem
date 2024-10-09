from fastapi import (
    APIRouter,
)


router = APIRouter(tags=["Лаб.Работа №4"], prefix="/lab4")


@router.get(
    "",
)
async def get_backpack():
    pass
