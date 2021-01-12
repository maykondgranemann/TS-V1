from app.back.dao.connection import get_connection


def set_seller(name: str, phone: str, mail: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO seller (name, telephone, email) VALUES ('{name}', '{phone}', '{mail}');")
    conn.commit()
    cursor.close()
    conn.close()

def get_seller() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT name, telephone, email FROM seller;')
    sellers = cursor.fetchall()
    cursor.close()
    conn.close()
    return sellers
