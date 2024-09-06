from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)

from src.schema.sort_schema import TimingsSort
from src.services.sort_service import SortingService


router = APIRouter(tags=["Лаб. работа №1"], prefix="/lab1")


def get_sorting_service():
    return SortingService()


@router.get("", response_model=TimingsSort)
async def get_timing_algorithm_sorting(
    size_massive: int = Query(
        ge=1,
        le=100_000,
        description="Количество элементов в массиве",
        default=10000,
    ),
    sort_percent: int = Query(
        ge=0,
        le=100,
        description="Насколько будет отсортирован входной массив",
        default=50,
    ),
    sorting_service: SortingService = Depends(get_sorting_service),
):
    try:
        return sorting_service.get_timings(size=size_massive, sort_percent=sort_percent)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
