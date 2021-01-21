from back.models.base_model import BaseModel
from back.dao.connection import Connection


class BaseDao:
    def __init__(self, type_model:BaseModel) -> None:
        self.__type_model = type_model

    # insert e update
    def save(self, model:BaseModel) -> None:
        try:
            with Connection() as conn:
                conn.add(model)
                conn.commit()
        except Exception as e:
            print(e)

    def read_all(self) -> list:
        try:
            with Connection() as conn:
                result = conn.query(self.__type_model).all()
                return result
        except Exception as e:
            print(e)

    def read_by_id(self, id:int) -> BaseModel:
        try:
            with Connection() as conn:
                result = conn.query(self.__type_model).filter_by(id=id).first()
                return result
        except Exception as e:
            print(e)

    def delete(self, model:BaseModel) -> None:
        try:
            with Connection() as conn:
                conn.delete(model)
                conn.commit()
        except Exception as e:
            print(e)
