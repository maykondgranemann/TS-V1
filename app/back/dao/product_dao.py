import psycopg2
from app.back.controllers.log_controller import create_log
from app.back.dao.connection import  _set_database, _connection_credentials
from app.back.models.product import Product

def set_product(product: Product) -> None:
    try:
        _set_database()
        with psycopg2.connect(_connection_credentials()) as conn:
            cur = conn.cursor()

            cur.execute(f"INSERT INTO product (name, description, price) VALUES ('{product.name}', '{product.description}', '{product.price}');")
            conn.commit()
    except:
        print('An unexpected error has occurred')


def get_products() -> list:
    products = []
    
    try:
        _set_database()
        with psycopg2.connect(_connection_credentials()) as conn:
            cur = conn.cursor()

            cur.execute(f"SELECT NAME, DESCRIPTION, PRICE, ID FROM product")
            result = cur.fetchall()
        
            for product in result:
                product = Product(product[0], product[1], product[2], product[3])
                products.append(product)
    except:
        print('An unexpected error has occurred')
    
    return products
