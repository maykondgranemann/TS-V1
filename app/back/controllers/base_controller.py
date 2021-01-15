from app.back.controllers.log_controller import LogController
log = LogController()
class BaseController:

    def __init__(self, dao, name_entity):
        self.name_entity = name_entity
        self.__dao = dao
    
    def create(self, model: object) -> None:
        self.__dao.create(model)
        log.create(f"Created {self.name_entity} - {model.name}")
    
    def read_by_id(self,id:int)-> object:
        object = self.__dao.read_by_id(id)
        log.create(f"Read {self.name_entity} - {object.name}")
        return object
        
    def read_all(self) -> None:
        result = self.__dao.read_all()
        log.create(f"Listed {self.name_entity}")
        return result
         
    def delete(self, id: int) -> None:
        object = self.__dao.read_by_id(id)
        self.__dao.delete(id)
        log.create(f"Deleted {self.name_entity} - {object.name}")


    def update(self, model: object) -> None:
        self.__dao.update(model)
        log.create(f"Updated {self.name_entity} - {model.name}")