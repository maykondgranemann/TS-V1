import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.base_model import BaseModel

class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def create(self, model: BaseModel) -> None:
        return self.__dao.save(model)

    def read_by_id(self, identifier:int) -> BaseModel:
        return self.__dao.read_by_id(identifier)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
    
    def update(self, model: BaseModel) -> None:
        self.__dao.save(model)