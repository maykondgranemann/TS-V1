from dao.session import Session
from models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model
    
    def save(self, model:BaseModel) -> int:
        with Session() as session:
            session.add(model)
            session.commit()
            session.flush()
            id = model.id
        return id
    
    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result

    def read_by_id(self, id:int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__type_model).filter_by(id=id).first()
        return result

    def delete(self, model:BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
