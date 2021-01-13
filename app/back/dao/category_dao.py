from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection
from app.back.models.category import Category

def set_category(category: Category) -> None:
    with get_connection() as conn:        
        cur = conn.cursor()
        cur.execute(f"INSERT INTO category (name, description) VALUES ('{category.name}', '{category.description}');")
        conn.commit()

def get_categories() -> list:
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute(f"SELECT NAME, DESCRIPTION, ID FROM category;")
        result = cur.fetchall()
        categories = []

        for item in result:
            category= Category(item[0], item[1], item[2])
            categories.append(category)

        return categories
