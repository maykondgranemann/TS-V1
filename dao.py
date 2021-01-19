from model import Seller
from session import Session


class SellerDao:
    def save(self, model: Seller) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_by_id(self, id_: str) -> Seller:
        with Session() as session:
            result = session.query(Seller).filter_by(id = id_).first()
        return result

    def read_all(self) -> list[Seller]:
        with Session() as session:
            result = session.query(Seller).all()
        return result

    def delete(self, model: Seller) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()

        