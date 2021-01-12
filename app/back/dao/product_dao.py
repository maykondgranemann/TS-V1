from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection

def set_product(name: str, description: str, price: float) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"INSERT INTO product (name, description, price) VALUES ('{name}', '{description}', '{price}');")
    conn.commit()

    cur.close()
    conn.close()


def get_products() -> list:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT NAME, DESCRIPTION, PRICE FROM product")
    products_list = cur.fetchall()

    cur.close()
    conn.close()

    return products_list
