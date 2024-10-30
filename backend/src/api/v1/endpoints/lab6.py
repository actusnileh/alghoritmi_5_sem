import random

from fastapi import (
    APIRouter,
    Query,
)

from src.services.avl_tree import (
    calculate_height,
    insert,
    remove,
    search,
    traverse_as_dict,
)


router = APIRouter(tags=["Лаб. работа №6 (AVL-Дерево)"], prefix="/lab_6")

avl_tree = None


@router.post("/clear")
async def clear():
    global avl_tree
    avl_tree = None
    return {"message": "AVL-дерево очищено"}


@router.post("/insert", response_model=dict)
async def insert_node(key: int = Query(..., description="Ключ для вставки")):
    global avl_tree
    avl_tree = insert(avl_tree, key)
    return {"message": f"Ключ {key} вставлен в AVL-дерево"}


@router.post("/del")
async def delete(
    del_key: int = Query(..., description="Элемент, который будет удален из дерева"),
):
    global avl_tree
    remove(avl_tree, del_key)
    return {"message": f"Ключ {del_key} удален из B-дерева"}


@router.get("/search", response_model=dict)
async def search_key(key: int = Query(..., description="Ключ для поиска")):
    """Поиск ключа в АВЛ-дереве"""
    global avl_tree

    result = search(avl_tree, key)
    if result:
        return {"message": f"Ключ {key} найден в AVL-дереве"}
    return {"message": f"Ключ {key} не найден"}


@router.get("/tree_structure", response_model=dict)
async def get_tree_structure():
    global avl_tree
    tree = traverse_as_dict(avl_tree)  # Используем метод для получения структуры
    return {"tree": tree}


@router.post("/random_fill")
async def random_fill(
    count: int = Query(10, description="Количество случайных ключей"),
):
    """Заполняет дерево случайными ключами"""
    global avl_tree
    keys = random.sample(range(1, 100), count)
    for key in keys:
        avl_tree = insert(avl_tree, key)  # Вставляем каждый случайный ключ в АВЛ-дерево
    return {"message": f"AVL-дерево заполнено {count} случайными ключами", "keys": keys}


@router.get("/height", response_model=dict)
async def get_tree_height():
    global avl_tree
    height = calculate_height(avl_tree)  # Необходимо реализовать calculate_height
    return {"height": height}
