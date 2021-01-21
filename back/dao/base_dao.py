from back.models.base_model import BaseModel
from back.dao.session import Session


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result

    def read_by_id(self, id: int) -> BaseModel:
        try:
            with Session() as session:
                model = session.query(self.__type_model).filter_by(id=id).first()
            return model
        except:
            raise NameError('Error, id must be an integer')
            
    def delete(self, model: BaseModel) -> None:
        try:
            with Session() as session:
                session.delete(model)
                session.commit()
        except:
            raise NameError('Error, id must be an object')
