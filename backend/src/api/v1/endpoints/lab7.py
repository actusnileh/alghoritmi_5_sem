import random

from fastapi import (
    APIRouter,
    Query,
)

from src.services.red_black_tree import RedBlackTree


router = APIRouter(tags=["Лаб. работа №7 (Красно-черное Дерево)"], prefix="/lab_7")

red_black_tree = RedBlackTree()


@router.post("/clear")
async def clear():
    global red_black_tree
    red_black_tree = RedBlackTree()
    return {"message": "Красно-черное дерево очищено"}


@router.post("/insert", response_model=dict)
async def insert_node(key: int = Query(..., description="Ключ для вставки")):
    red_black_tree.insert(key)
    return {"message": f"Ключ {key} вставлен в красно-черное дерево"}


@router.post("/del", response_model=dict)
async def delete_node(
    del_key: int = Query(..., description="Элемент, который будет удален из дерева"),
):
    red_black_tree.delete(del_key)
    return {"message": f"Ключ {del_key} удален из красно-черного дерева"}


@router.get("/search", response_model=dict)
async def search_key(key: int = Query(..., description="Ключ для поиска")):
    node = red_black_tree.search(key)
    if node:
        return {"message": f"Ключ {key} найден в дереве"}
    return {"message": f"Ключ {key} не найден в дереве"}


@router.get("/tree_structure", response_model=dict)
async def get_tree_structure():
    tree = red_black_tree.traverse_as_dict(red_black_tree.root)
    return {"tree": tree}


@router.post("/random_fill", response_model=dict)
async def random_fill(
    count: int = Query(10, description="Количество случайных ключей"),
):
    keys = random.sample(range(-100, 100), count)
    for key in keys:
        red_black_tree.insert(key)
    return {
        "message": f"Красно-черное дерево заполнено {count} случайными ключами",
        "keys": keys,
    }
