from backend.models.base_model import BaseModel
from backend.dao.db_config import Session


class BaseDao:
    def __init__(self, type_model):
        self.__type_model = type_model

    def save(self, model: BaseModel) -> None:
        try:
            with Session() as session:
                session.add(model)
                session.commit()
        except Exception as e:
            print(e)

    def read_all(self) -> list:
        try:
            with Session() as session:
                list_result = session.query(self.__type_model).order_by(self.__type_model.id.desc()).all()
            return list_result
        except Exception as e:
            print(e)

    def read_by_id(self, id):
        try:
            with Session() as session:
                result = session.query(self.__type_model).filter_by(id=id).first()
            return result
        except Exception as e:
            print(e)

    def delete(self, model: BaseModel) -> None:
        try:
            with Session() as session:
                session.delete(model)
                session.commit()
        except Exception as e:
            print(e)