from back.models.base_model import BaseModel
from back.dao.session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BaseDao:
    def __init__(self, type_model):
        self.__type_model = type_model

    def save(self, model:BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            sellers = session.query(self.__type_model).all()
        return sellers

    def read_by_id(self, id:int) -> BaseModel:
        with Session() as session:
            seller = session.query(self.__type_model).filter_by(id=id).first()
        return seller

    def update(self, model:BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def delete(self, model:BaseModel)-> None:
        with Session() as session:
            session.delete(model)
            session.commit()