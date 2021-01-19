from typing import ClassVar

from app.database.models import BaseModel
from app.database.session import Session


class BaseDao:
    def __init__(self, model_type: ClassVar):
        self.__model_type = model_type

    @staticmethod
    def save(model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__model_type).all()
        return result

    def read_by_id(self, id: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__model_type).filter_by(id=id).one()
        return result

    @staticmethod
    def delete(model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
