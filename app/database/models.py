from typing import ClassVar

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base

from app.database.session import Session

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


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
