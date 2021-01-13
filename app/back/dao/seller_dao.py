from app.back.dao.connection import get_connection
from app.back.models.seller import Seller

def set_seller(seller: Seller) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO seller (name, telephone, email) VALUES ('{seller.name}', '{seller.phone}', '{seller.mail}');")
        conn.commit()


def get_seller() -> list:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT name, telephone, email, id FROM seller;')
        result = cursor.fetchall()
        sellers = []

        for item in result:
            seller = Seller(item[0], item[1], item[2], item[3])
            sellers.append(seller)

        return sellers
