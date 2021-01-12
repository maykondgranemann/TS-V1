from app.back.controllers.log_controller import create_log
from app.back.dao.connection import get_connection


def set_marketplace(name: str, description: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO marketplace (name, description) VALUES ('{name}', '{description})';")
    conn.commit()
    cursor.close()
    conn.close()

def get_marketplace() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT name, description FROM marketplace;')
    marketplaces = cursor.fetchall()
    cursor.close()
    conn.close()
    return marketplaces
