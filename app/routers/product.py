from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

import db_on_mem

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    price: int


@router.get("/")
async def get_all_products():
    return db_on_mem.get_products()

@router.post("/")
async def add_product(id: int = 3, name: str = 'nuvo', price: int = 10000):
    product = {
        "id": int(id),
        "name": name,
        "price": int(price)
    }
    return db_on_mem.add_product(product)
@router.put("/{product_id}")
async def update_product(product_id: str , product: Product):
    print(product.dict())
    return db_on_mem.update_product(int(product_id), product.dict())

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    return db_on_mem.delete_product(product_id)