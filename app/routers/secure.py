from fastapi import APIRouter, Depends

from auth import get_user

router = APIRouter()

@router.get("/")
async def get_testrouter(user: dict = Depends(get_user)):
    return user