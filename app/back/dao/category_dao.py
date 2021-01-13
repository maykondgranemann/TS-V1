import psycopg2
from app.back.controllers.log_controller import create_log
from app.back.dao.connection import _set_database, _connection_credentials
from app.back.models.category import Category

def set_category(category: Category) -> None:
    try:
        _set_database()
        with psycopg2.connect(_connection_credentials()) as conn:       
            cur = conn.cursor()
            cur.execute(f"INSERT INTO category (name, description) VALUES ('{category.name}', '{category.description}');")
            conn.commit()
    except:
        print('An unexpected error has occurred')


def get_categories() -> list:
    categories = []
    try:
        _set_database()
        with psycopg2.connect(_connection_credentials()) as conn:
            cur = conn.cursor()

            cur.execute(f"SELECT NAME, DESCRIPTION, ID FROM category;")
            result = cur.fetchall()
            

            for item in result:
                category= Category(item[0], item[1], item[2])
                categories.append(category)
    except:
        print('An unexpected error has occurred')

    return categories
