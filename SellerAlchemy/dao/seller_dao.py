from SellerAlchemy.dao.session import Session
from SellerAlchemy.models.seller import Seller

class SellerDao:
    def save(self, seller: Seller) -> None:
        with Session() as session:
            session.add(seller)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(Seller).all()
        return result

    def read_by_id(self, id: int) -> Seller:
        with Session() as session:
            result = session.query(Seller).filter_by(id=id).first()
        return result

    def delete(self, seller: Seller) -> None:
        with Session() as session:
            session.delete(seller)
            session.commit()