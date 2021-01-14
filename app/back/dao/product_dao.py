import psycopg2
from app.back.controllers.log_controller import create_log
from app.back.dao.connection import  set_database, connection_credentials
from app.back.models.product import Product

def set_product(product: Product) -> None:
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()

            cur.execute(f"INSERT INTO product (name, description, price) VALUES ('{product.name}', '{product.description}', '{product.price}');")
            conn.commit()
    except:
        print('An unexpected error has occurred')


def get_products() -> list:
    products = []
    
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()

            cur.execute(f"SELECT NAME, DESCRIPTION, PRICE, ID FROM product")
            result = cur.fetchall()
        
            for product in result:
                product = Product(product[0], product[1], product[2], product[3])
                products.append(product)
    except:
        print('An unexpected error has occurred')
    
    return products


def upd_product(product: Product) -> None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f"UPDATE product SET name='{product.name}', description='{product.description}', price='{product.price}' WHERE id={product.id}")
    except:
        print('An unexpected error has occurred')


def del_product(id: str) -> None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f"DELETE FROM product WHERE id={id}")
    except:
        print('An unexpected error has occurred')