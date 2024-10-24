import random

from fastapi import (
    APIRouter,
    Query,
)

from src.services.b_tree import BTree


router = APIRouter(tags=["Лаб. работа №5 (Б-Дерево)"], prefix="/lab_5")

btree = BTree(t=2)


@router.post("/clear")
async def clear():
    global btree
    btree = BTree(t=2)
    return {"message": "B-дерево очищено"}


@router.post("/insert", response_model=dict)
async def insert_node(key: int = Query(..., description="Ключ для вставки")):
    btree.insert(key)
    return {"message": f"Ключ {key} вставлен в B-дерево"}


@router.get("/search", response_model=dict)
async def search_key(key: int = Query(..., description="Ключ для поиска")):
    result = btree.search(key)
    if result:
        return {"message": f"Ключ {key} найден в B-дереве"}
    return {"message": f"Ключ {key} не найден"}


@router.get("/tree_structure", response_model=dict)
async def get_tree_structure():
    tree = btree.traverse_as_dict()
    return {"tree": tree}


@router.post("/random_fill")
async def random_fill(
    count: int = Query(10, description="Количество случайных ключей"),
):
    keys = random.sample(range(-100, 100), count)
    for key in keys:
        btree.insert(key)
    return {"message": f"B-дерево заполнено {count} случайными ключами", "keys": keys}


@router.post("/del")
async def delete(
    del_key: int = Query(..., description="Элемент, который будет удален из дерева"),
):
    btree.delete(del_key)
    return {"message": f"Ключ {del_key} удален из B-дерева"}


@router.post("/search")
async def search(
    search_key: int = Query(..., description="Элемент, который найден в дереве"),
):
    result = btree.search(search_key)
    if result:
        return {"message": f"Ключ {search_key} найден в B-дереве"}
    else:
        return {"message": f"Ключ {search_key} не найден в B-дереве"}
