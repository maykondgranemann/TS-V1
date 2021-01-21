class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def save(self, model: object)->None:
        self.__dao.save(model)

    def read_by_id(self,id:int)-> object:
        return self.__dao.read_by_id(id)

    def read_all(self)->list:
        return self.__dao.read_all()

    def delete(self, id:int)->None:
        model = self.read_by_id(id)
        self.__dao.delete(model)
