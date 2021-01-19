from backend.dao.session import Session
from backend.models.seller import SellerModel


class SellerDao:
    def save(self, model: object) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(SellerModel).all()
            return result

    def read_by_id(self, id: int) -> object:
        with Session() as session:
            result = session.query(SellerModel).filter_by(id=id).first()
            return result

    def delete(self, model: object) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
