from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.crud.category import create_category, get_categories, get_category, update_category, delete_category

router = APIRouter()

# Create a new category
@router.post("/", response_model=CategoryResponse)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

# Get all categories
@router.get("/", response_model=list[CategoryResponse])
def fetch_all_categories(db: Session = Depends(get_db)):
    return get_categories(db)

# Get a single category by ID
@router.get("/{category_id}", response_model=CategoryResponse)
def fetch_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# Update a category
@router.put("/{category_id}", response_model=CategoryResponse)
def modify_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    updated_category = update_category(db, category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

# Delete a category
@router.delete("/{category_id}", response_model=CategoryResponse)
def remove_category(category_id: int, db: Session = Depends(get_db)):
    deleted_category = delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
