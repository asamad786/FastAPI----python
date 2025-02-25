from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

# Create a new category
def create_category(db: Session, category_data: CategoryCreate):
    new_category = Category(name=category_data.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

# Get all categories
def get_categories(db: Session):
    return db.query(Category).all()

# Get a single category by ID
def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

# Update a category
def update_category(db: Session, category_id: int, category_data: CategoryUpdate):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        category.name = category_data.name
        db.commit()
        db.refresh(category)
    return category

# Delete a category
def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category
