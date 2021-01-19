from backend.models.base_model import BaseModel
class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def save(self, model: BaseModel) -> None:
        self.__dao.save(model)

    def read_by_id(self, id: int) -> BaseModel:
        objetc_by_id = self.__dao.read_by_id(id)
        return objetc_by_id

    def read_all(self) -> list:
        list_all = self.__dao.read_all()
        return list_all

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
