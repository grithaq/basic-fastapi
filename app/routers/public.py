from fastapi import APIRouter, Depends

from auth import get_user
from db_on_mem import get_products

router = APIRouter()

@router.get("/")
async def get_testroute():
    return "OK"

@router.get("/products")
async def get_all_products():
    return get_products()