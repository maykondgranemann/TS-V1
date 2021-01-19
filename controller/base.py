
class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def delete(self, model) -> None:
        self.__dao.delete(model)
    
    def read_all(self) -> list:
        result = self.__dao.read_all()
        return result
    
    def create(self, model) -> None:
        self.__dao.save(model)