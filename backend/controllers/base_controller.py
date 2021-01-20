from backend.daos.base_dao import BaseDao
from backend.models.base_model import BaseModel

class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def create(self, model: BaseModel) -> None:
        return self.__dao.save(model)

    def read_by_id(self, id: int) -> object:
        return self.__dao.read_by_id(id)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)

    def update(self, model: BaseModel) -> None:
        self.__dao.save(model)
