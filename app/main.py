from fastapi import FastAPI
from app.routers import category
from app.routers import product

app = FastAPI()

app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(product.router, prefix="/products", tags=["Products"])


@app.get("/")
def root():
    return {"message": "FastAPI with MySQL is running!"}
