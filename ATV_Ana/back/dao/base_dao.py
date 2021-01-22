from ATV_Ana.back.models.base_model import BaseModel
from ATV_Ana.back.dao.session import Session


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def create_update(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            sellers = session.query(self.__type_model).all()
        return sellers

    def read_by_id(self, id_: int):
        with Session() as session:
            sel = session.query(self.__type_model).filter_by(id=id_).first()
        return sel

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()

