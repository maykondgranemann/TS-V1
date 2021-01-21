from luciana.models.base_model import BaseModel

class BaseController: 
    def __init__(self, dao):
        self.__dao = dao()

    def save(self, model: BaseModel) -> None:
        self.__dao.save(model)

    def read_by_id(self, id: int) -> object:
        result = self.__dao.read_by_id(id)

    def read_all(self) -> list:
        result = self.__dao.read_all()
        return result        

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)