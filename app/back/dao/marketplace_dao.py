from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection
from app.back.models.marketplace import Marketplace


def set_marketplace(marketplace: Marketplace) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');")
    conn.commit()
    cursor.close()
    conn.close()

def get_marketplace() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT name, description, id FROM marketplace;')
    result = cursor.fetchall()
    marketplaces = []

    for item in result:
        marketplace = Marketplace(item[0], item[1], item[2])
        marketplaces.append(marketplace)
        
    cursor.close()
    conn.close()
    return marketplaces
