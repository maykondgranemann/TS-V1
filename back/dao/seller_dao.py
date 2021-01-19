from back.dao.connection import Connection
from back.models.seller_model import Seller


class SellerDao:
    def save(self, model:Seller) -> None:
        with Connection() as conn:
            conn.add(model)
            conn.commit()

    def read_all(self, model:Seller) -> list:
        with Connection() as conn:
            result = conn.query(model).all()
            return result

    def read_by_id(self, id:int, model: Seller) -> Seller:
        with Connection() as conn:
            result = conn.query(model).filter_by(id=id).first()
            return result

    def delete(self, model:Seller) -> None:
        with Connection() as conn:
            conn.delete(model)
            conn.commit()

