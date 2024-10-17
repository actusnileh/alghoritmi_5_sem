# src/api/btree_router.py

from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from src.services.b_tree import BTree
from src.schema.btree_schema import BTreeResponse, KeyValuePair

router = APIRouter(tags=["Лаб. работа №5 (Б-Дерево)"], prefix="/lab_5")

# Инициализация B-дерева с порядком t
btree = BTree(t=3)


@router.post("/insert", response_model=BTreeResponse)
async def insert_node(
    key: int = Query(..., description="Ключ для вставки"),
    value: int = Query(..., description="Значение для вставки"),
):
    btree.insert_key((key, value))
    return BTreeResponse(keys=[KeyValuePair(key=key, value=value)])


@router.get("/search", response_model=Optional[BTreeResponse])
async def search_key(
    key: int = Query(..., description="Ключ для поиска"),
):
    result = btree.search_key(key)
    if result is None:
        raise HTTPException(status_code=404, detail="Key not found")
    node, index = result
    return BTreeResponse(
        keys=[KeyValuePair(key=node.keys[index][0], value=node.keys[index][1])]
    )


@router.get("/", response_model=BTreeResponse)
async def get_tree():
    def get_all_keys(node):
        keys = []
        if node:
            keys.extend(node.keys)
            for child in node.children:
                keys.extend(get_all_keys(child))
        return keys

    keys = get_all_keys(btree.root)
    return BTreeResponse(keys=[KeyValuePair(key=k[0], value=k[1]) for k in keys])
