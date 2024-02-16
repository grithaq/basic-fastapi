from fastapi import FastAPI, Depends

from routers import public, secure, product
from auth import get_user

app = FastAPI()

app.include_router(
    public.router, prefix="/api/v1/public"
)

app.include_router(
    secure.router, prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)

app.include_router(
    product.router, prefix="/api/v1/product"
)