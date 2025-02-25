from pydantic import BaseModel
from typing import Optional

# Schema for creating a category
class CategoryCreate(BaseModel):
    name: str

# Schema for updating a category
class CategoryUpdate(BaseModel):
    name: str

# Schema for returning category data
class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
