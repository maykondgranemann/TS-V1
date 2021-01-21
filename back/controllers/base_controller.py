
class BaseController:
    def __init__(self, dao):
        self.dao = dao

    def save(self, model: object) -> None:
        self.dao.save(model)

    def read_all(self) -> list:
        return self.dao.read_all()

    def read_by_id(self, id: int) -> object:
        return self.dao.read_by_id(id)

    def delete(self, model: object) -> None:
        self.dao.delete(model)
