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
    elements, directions = LCSService().lcs_table(element_1, element_2)
    all_lcs = LCSService().find_all_lcs(
        elements, element_1, element_2, len(element_1), len(element_2)
    )

    return LCSResponse(elements=elements, directions=directions, all_lcs=all_lcs)
