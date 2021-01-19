from backend.dao.session import Session
from backend.models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model):
        self.type_model = type_model

    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.type_model).all()
            return result

    def read_by_id(self, id: int) -> object:
        with Session() as session:
            result = session.query(self.type_model).filter_by(id=id).first()
            return result

    def delete(self, model: object) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
