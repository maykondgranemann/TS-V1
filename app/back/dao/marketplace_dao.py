import psycopg2
from app.back.controllers.log_controller import create_log
from app.back.dao.connection import set_database, connection_credentials
from app.back.models.marketplace import Marketplace


def set_marketplace(marketplace: Marketplace) -> None:
    try: 
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');")
            conn.commit()
    except Exception as error:
        print(error)

def get_marketplace() -> list:
    marketplaces = []
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT name, description, id FROM marketplace;')
            result = cursor.fetchall()
            
            for item in result:
                marketplace = Marketplace(item[0], item[1], item[2])
                marketplaces.append(marketplace)
    except Exception as error:
        print(error)   
             
    return marketplaces

def del_marketplace(id: str):
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM marketplace WHERE id='{id}'")
    except Exception as error:
        print(error)

def upd_marketplace(marketplace: Marketplace):
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE marketplace SET name='{marketplace.name}',description='{marketplace.description}'WHERE id='{marketplace.id}'")
    except Exception as error:
        print(error)