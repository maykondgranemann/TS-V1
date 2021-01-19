# Importar as características da BaseModel
from ..model.model_base import BaseModel

# Importar a classe Session em session.py
from .session import Session

# Criar classe base para a DAO 
class DaoBase:
    def __init__(self, type_model):
        self.__type_model = type_model

    def save(self, model:BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result

    def read_by_id(self, id_:int) -> BaseModel:
        with Session() as session:
            result = session(self.__type_model).filter_by(id=id_).first()
        return result

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
