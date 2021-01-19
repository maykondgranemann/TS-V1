from back.models.base_model import BaseModel
from back.dao.base_dao import BaseDao


class BaseController:
    def __init__(self, type_dao: BaseDao) -> None:
        self.__type_dao = type_dao

    def create(self, model: BaseModel) -> None:
        self.__type_dao().save(model)
    
    def update(self, model:BaseModel) -> None:
        self.__type_dao().save(model)

    def read_by_id(self, id:int) -> BaseModel:
        seller = self.__type_dao().read_by_id(id)
        return seller
    
    def read_all(self) -> list:
        sellers = self.__type_dao().read_all()
        return sellers
    
    def delete(self, model: BaseModel) -> None:
        self.__type_dao().delete(model)