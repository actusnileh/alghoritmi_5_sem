import random

from fastapi import (
    APIRouter,
    Query,
)

from src.services.avl_tree import AVLTree


router = APIRouter(tags=["Лаб. работа №6 (AVL-Дерево)"], prefix="/lab_6")

avl_tree = AVLTree()
root = None


@router.post("/clear")
async def clear():
    global avl_tree, root
    avl_tree = AVLTree()
    root = None
    return {"message": "AVL-дерево очищено"}


@router.post("/insert", response_model=dict)
async def insert_node(key: int = Query(..., description="Ключ для вставки")):
    global root
    root = avl_tree.insert(root, key)
    return {"message": f"Ключ {key} вставлен в AVL-дерево"}


@router.post("/del", response_model=dict)
async def delete(
    del_key: int = Query(..., description="Элемент, который будет удален из дерева"),
):
    global root
    root = avl_tree.delete(root, del_key)
    return {"message": f"Ключ {del_key} удален из AVL-дерева"}


@router.get("/search", response_model=dict)
async def search_key(key: int = Query(..., description="Ключ для поиска")):
    def search(node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return search(node.left, key)
        else:
            return search(node.right, key)

    global root
    found = search(root, key)
    if found:
        return {"message": f"Ключ {key} найден в AVL-дереве"}
    return {"message": f"Ключ {key} не найден"}


@router.get("/tree_structure", response_model=dict)
async def get_tree_structure():
    global root
    tree = avl_tree.traverse_as_dict(root)
    return {"tree": tree}


@router.post("/random_fill", response_model=dict)
async def random_fill(
    count: int = Query(10, description="Количество случайных ключей"),
):
    global root
    keys = random.sample(range(1, 100), count)
    for key in keys:
        root = avl_tree.insert(root, key)
    return {"message": f"AVL-дерево заполнено {count} случайными ключами", "keys": keys}
