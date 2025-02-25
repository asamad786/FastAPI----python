from app.db import SessionLocal
from sqlalchemy.sql import text  # Import text() function

# Test the database connection
def test_db_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # Use text() for raw SQL query
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    finally:
        db.close()

# Run the test
if __name__ == "__main__":
    test_db_connection()
