from backend.models.base_model import BaseModel
from backend.dao.base_dao import BaseDao
class BaseController:
    def __init__(self, dao):
        if isinstance(dao, BaseDao):
            self.__dao = dao
        else:
            raise ValueError('dao must receive a valid dao')
        

    def save(self, model: BaseModel) -> None:
        if isinstance(model, BaseModel):
            self.__dao.save(model)
        else:
            raise ValueError('the save method must receive object of a Class')
    def read_by_id(self, id: int) -> BaseModel:
        objetc_by_id = self.__dao.read_by_id(id)
        return objetc_by_id

    def read_all(self) -> list:
        list_all = self.__dao.read_all()
        return list_all

    def delete(self, model: BaseModel) -> None:
        if isinstance(model, BaseModel):
            self.__dao.delete(model)
        else:
            raise ValueError("The save method must receive object of a Class")
