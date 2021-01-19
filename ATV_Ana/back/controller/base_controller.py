class BaseController:
    def __init__(self, dao) -> None:
        self.__dao = dao

    def create_update(self, model: object) -> None:
        return self.__dao.create_update(model)

    def read_by_id(self, id: int) -> object:
        return self.__dao.read_by_id(id)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def delete(self, id: int) -> None:
        self.__dao.delete(id)
