from model.base_model import BaseModel

class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def save(self, model: BaseModel) -> None:
        self.__dao.save(model)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def read_by_id(self, id: int) -> object:
        return self.__dao.read_by_id(id)

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)