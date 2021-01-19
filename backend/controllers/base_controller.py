from backend.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao):
        self.dao = dao()

    def save(self, model: BaseModel) -> None:
        self.dao.save(model)

    def read_all(self) -> list:
        result = self.dao.read_all()
        return result

    def read_by_id(self, id: int) -> object:
        result = self.dao.read_by_id(id)
        return result

    def delete(self, model: BaseModel) -> None:
        self.dao.delete(model)
