from fastapi import (
    APIRouter,
    Query,
)

from src.schema.lcs_schema import LCSResponse
from src.services.lcs_service import LCSService


router = APIRouter(tags=["Лаб.Работа №3"], prefix="/lab3")


@router.get("", response_model=LCSResponse)
async def get_lcs(
    element_1: str = Query(description="Первый элемент"),
    element_2: str = Query(description="Второй элемент"),
):
    return LCSResponse(data=LCSService().lcs_table(element_2, element_1))
