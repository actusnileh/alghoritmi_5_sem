from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)

from src.schema.iter_matrix_schema import IterMatrix
from src.services.iter_matrix_service import IterMatrixService


router = APIRouter(tags=["Лаб. работа №2"], prefix="/lab2")


def iter_matrix_service():
    return IterMatrixService()


@router.get("", response_model=IterMatrix)
async def get_iter_matrix(
    p: str = Query(
        ...,
        description="Список размеров матриц, разделенных запятыми, например: 30,35,15,5,10,20,25",
    ),
    iter_matrix_service: IterMatrixService = Depends(iter_matrix_service),
):
    p = list(map(int, p.split(",")))
    matrix, k = iter_matrix_service.matrix_chain_order(p)
    brackets = iter_matrix_service.optimal_parens(k, 0, len(p) - 2)

    return IterMatrix(
        matrix=matrix,
        k=k,
        optimal_brackets=brackets,
    )