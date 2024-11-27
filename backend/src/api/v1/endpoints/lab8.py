from fastapi import (
    APIRouter,
    HTTPException,
)

from src.services.lcs_suffix import STree


router = APIRouter(tags=["Лаб. работа №8"], prefix="/lab8")


@router.post("")
async def get_lcs_suffix(strings: list[str]):
    if not strings:
        raise HTTPException(status_code=400, detail="List of strings cannot be empty")

    try:
        st = STree(strings)
        lcs = st.lcs()
        tree_structure = st.get_tree_structure()
        return {
            "lcs": lcs,
            "structure": tree_structure,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
