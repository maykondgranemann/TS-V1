from models.base_model import BaseModel


class BaseController:
    def __init__(self, dao:BaseModel) -> None:
        self.__dao = dao
    
    def save(self, model:BaseModel) -> None:
        self.__dao.save(model)
    
    def read_by_id(self, id:int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        return result
    
    def read_all(self) -> list:
        list_all = self.__dao.read_all()
        return list_all
    
    def delete(self, id:int) -> None:
        model = self.__dao.read_by_id(id)
        self.__dao.delete(model)