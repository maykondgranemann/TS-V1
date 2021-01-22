from backend.dao.session import Session
from backend.models.base_model import BaseModel
from sqlalchemy import inspect


class BaseDao:
    def __init__(self, type_model):
        self.type_model = type_model

    def save(self, model: BaseModel) -> tuple:
        with Session() as session:
            session.add(model)
            session.commit()
            id_ = model.id
            state = inspect(model).persistent
        return id_, state

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.type_model).all()
            return result

    def read_by_id(self, id_: int) -> object:
        int(id_)
        with Session() as session:
            result = session.query(self.type_model).filter_by(id=id_).first()
            return result

    def delete(self, model: object) -> bool:
        with Session() as session:
            session.delete(model)
            session.commit()
            state = inspect(model).detached
        return state
