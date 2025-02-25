from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import Response
from app.db import SessionLocal
from app.crud.product import create_product, get_products, get_product, update_product, delete_product
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductResponse)
def create_product_api(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_api(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product_api(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=204)
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    deleted_product = delete_product(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return Response(status_code=204)
