import psycopg2
from app.back.dao.connection import _set_database, _connection_credentials
from app.back.models.seller import Seller

def set_seller(seller: Seller) -> None:
    try:
        _set_database()
        with psycopg2.connect(_connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO seller (name, telephone, email) VALUES ('{seller.name}', '{seller.phone}', '{seller.mail}');")
            conn.commit()
    except:
        print('An unexpected error has occurred')
        

def get_seller() -> list:
    sellers = []
    try:
        _set_database()
        with psycopg2.connect(_connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT name, telephone, email, id FROM seller;')
            result = cursor.fetchall()
            
            for item in result:
                seller = Seller(item[0], item[1], item[2], item[3])
                sellers.append(seller)
    except:
        print('An unexpected error has occurred')

    return sellers
