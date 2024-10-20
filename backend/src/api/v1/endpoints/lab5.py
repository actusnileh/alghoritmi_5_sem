from random import SystemRandom

from fastapi import (
    APIRouter,
    HTTPException,
    Query,
)

from src.services.b_tree import BTree


router = APIRouter(tags=["Лаб. работа №5 (Б-Дерево)"], prefix="/lab_5")

btree = BTree(t=2)


@router.post("/clear")
async def clear():
    global btree
    try:
        btree = BTree(t=2)
        return {"message": "Дерево очищено"}
    except Exception as e:
        return {"message": "Ошибка при очистке дерева", "error": str(e)}, 500


@router.post("/insert", response_model=dict)
async def insert_node(key: int = Query(..., description="Ключ для вставки")):
    btree.insert_key(key)
    return {"message": f"Ключ {key} вставлен"}


@router.get("/search", response_model=dict)
async def search_key(key: int = Query(..., description="Ключ для поиска")):
    result = btree.search_key(key)
    if result is None:
        raise HTTPException(status_code=404, detail="Ключ не найден")
    return {"message": f"Ключ {key} найден"}


@router.get("/tree_structure", response_model=dict)
async def get_tree_structure():
    btree.print_tree(btree.root)

    def build_tree(node):
        if not node.keys:
            return None

        return {
            "name": f"Keys: {', '.join(map(str, node.keys))}",
            "children": [
                build_tree(child)
                for child in node.children
                if build_tree(child) is not None
            ],
        }

    return build_tree(btree.root)


@router.post("/random_fill")
def random_fill():
    for _ in range(10):
        key = SystemRandom().randint(0, 10)
        btree.insert_key(key)
    return {"message": "Дерево заполнено случайными значениями"}
