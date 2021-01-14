import psycopg2
from app.back.dao.connection import set_database, connection_credentials
from app.back.models.seller import Seller

def set_seller(seller: Seller) -> None:
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO seller (name, telephone, email) VALUES ('{seller.name}', '{seller.phone}', '{seller.mail}');")
            conn.commit()
    except Exception as error:
        print(error)
        

def get_seller() -> list:
    sellers = []
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT name, telephone, email, id FROM seller;')
            result = cursor.fetchall()
            
            for item in result:
                seller = Seller(item[0], item[1], item[2], item[3])
                sellers.append(seller)
    except Exception as error:
        print(error)

    return sellers

def del_seller(id: str):
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM seller WHERE id='{id}'")
    except Exception as error:
        print(error)

def upd_seller(seller: Seller):
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE seller SET name='{seller.name}', telephone='{seller.phone}', email='{seller.mail}' WHERE id={seller.id}")
    except Exception as error:
        print(error)