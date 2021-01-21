import sys
sys.path.append('')
from model.base_model import BaseModel

class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def save(self, model: BaseModel) -> None:
        return self.__dao.create(model)

    def read_by_id(self, id: int) -> object:
        return self.__dao.read_by_id(id)

    def read_all(self, id: int) -> list:
        return self.__dao.read_all()

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(id)