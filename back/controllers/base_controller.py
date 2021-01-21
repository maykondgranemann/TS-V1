from back.models.base_model import BaseModel
from back.dao.base_dao import BaseDao


class BaseController:
    def __init__(self, type_dao: BaseDao) -> None:
        if isinstance(type_dao, BaseDao):
            self.__type_dao = type_dao
        else:
            raise TypeError("Type DAO must be a class BaseDao")

    def create(self, model: BaseModel) -> None:
        if isinstance(model, BaseModel):
            self.__type_dao.save(model)
        else:
            raise TypeError("Model must be a class BaseModel")

    def update(self, model:BaseModel) -> None:
        if isinstance(model, BaseModel):
            self.__type_dao.save(model)
        else:
            raise TypeError("Model must be a class BaseModel")

    def read_by_id(self, id:int) -> BaseModel:
        if isinstance(id, int):
            seller = self.__type_dao.read_by_id(id)
            return seller
        else:
            raise TypeError("ID must be a class Interger")
        
    def read_all(self) -> list:
        sellers = self.__type_dao.read_all()
        return sellers
    
    def delete(self, model: BaseModel) -> None:
        if isinstance(model, BaseModel):
            self.__type_dao.delete(model)
        else:
            raise TypeError("Model must be a class BaseModel")
