from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection
from app.back.models.product import Product

def set_product(product: Product) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"INSERT INTO product (name, description, price) VALUES ('{product.name}', '{product.description}', '{product.price}');")
    conn.commit()

    cur.close()
    conn.close()


def get_products() -> list:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT NAME, DESCRIPTION, PRICE, ID FROM product")
    result = cur.fetchall()
    products = []

    for product in result:
        product = Product(product[0], product[1], product[2], product[3])
        products.append(product)

    cur.close()
    conn.close()

    return products
