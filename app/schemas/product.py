from pydantic import BaseModel
from typing import Optional
from app.schemas.category import CategoryResponse

class ProductBase(BaseModel):
    name: str
    price: float
    category_id: int
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    description: Optional[str] = None

class ProductResponse(ProductBase):
    id: int
    category: CategoryResponse

    class Config:
        from_attributes = True
