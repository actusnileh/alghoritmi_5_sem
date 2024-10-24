import random

from fastapi import (
    APIRouter,
    Query,
)

from src.services.b_tree import BTree


router = APIRouter(tags=["Лаб. работа №5 (Б-Дерево)"], prefix="/lab_5")

# Инициализация B-дерева с минимальной степенью 2
btree = BTree(t=2)


@router.post("/clear")
async def clear():
    """Очистка B-дерева"""
    global btree
    btree = BTree(t=2)  # Пересоздаем дерево с той же степенью
    return {"message": "B-дерево очищено"}


@router.post("/insert", response_model=dict)
async def insert_node(key: int = Query(..., description="Ключ для вставки")):
    """Вставка ключа в B-дерево"""
    btree.insert(key)
    return {"message": f"Ключ {key} вставлен в B-дерево"}


@router.get("/search", response_model=dict)
async def search_key(key: int = Query(..., description="Ключ для поиска")):
    """Поиск ключа в B-дереве"""
    result = btree.search(key)
    if result:
        return {"message": f"Ключ {key} найден в B-дереве"}
    return {"message": f"Ключ {key} не найден"}


@router.get("/tree_structure", response_model=dict)
async def get_tree_structure():
    """Возвращает текущую структуру B-дерева"""
    tree = btree.traverse_as_dict()  # Используем новый метод для получения структуры
    return {"tree": tree}


@router.post("/random_fill")
async def random_fill(
    count: int = Query(10, description="Количество случайных ключей"),
):
    """Заполняет дерево случайными ключами"""
    keys = random.sample(range(1, 100), count)
    for key in keys:
        btree.insert(key)
    return {"message": f"B-дерево заполнено {count} случайными ключами", "keys": keys}
