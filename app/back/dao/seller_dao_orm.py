import sys
sys.path.append('.')

from app.back.dao.session import Session
from app.back.models.seller_orm import Seller

class SellerDao:
    def read_all(self):
        with Session() as session:
            result = session.query(Seller).all()
        return result

    def read_by_id(self, id: int):
        with Session() as session:
            result = session.query(Seller).filter_by(id=id).first()
        return result

    def save(self, model: Seller):
        with Session() as session:
            session.add(model)
            session.commit()

    def delete(self, model):
        with Session() as session:
            session.delete(model)
            session.commit()

