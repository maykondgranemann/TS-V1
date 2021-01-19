from models.seller import Seller
from dao.session import Session


class SellerDao:
    def create(self, seller: Seller) -> None:
        with Session() as session:
            session.add(seller)
            session.commit()

    def update(self, seller: Seller) -> None:
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
