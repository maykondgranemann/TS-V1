from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection

def set_category(name: str, description: str) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"INSERT INTO category (name, description) VALUES ({name}, {description});")
    conn.commit()

    cur.close()
    conn.close()


def get_categories() -> list:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT NAME, DESCRIPTION FROM category;")
    categories_list = cur.fetchall()

    cur.close()
    conn.close()

    return categories_list
