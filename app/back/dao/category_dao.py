from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection
from app.back.models.category import Category

def set_category(category: Category) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"INSERT INTO category (name, description) VALUES ('{category.name}', '{category.description}');")
    conn.commit()

    cur.close()
    conn.close()


def get_categories() -> list:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT NAME, DESCRIPTION, ID FROM category;")
    result = cur.fetchall()
    categories = []

    for item in result:
        category= Category(item[0], item[1], item[2])
        categories.append(category)


    cur.close()
    conn.close()

    return categories
