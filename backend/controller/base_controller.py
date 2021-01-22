import sys
sys.path.append('.')

from backend.models.base_model import BaseModel
from backend.dao.base_dao import BaseDao

class BaseController:  
    def __init__(self, dao):
        self.__dao = dao()
        
    def save_ctrl(self, model: BaseModel) -> None:
        self.__dao.save_dao(model)

    def read_all_ctrl(self) -> list:
        result = self.__dao.read_all_dao()
        return result

    def read_by_id_ctrl(self, id:int) -> object:
        result = self.__dao.read_by_id_dao(id)
        return result

    def delete_ctrl(self, model: BaseModel) -> None:
        self.__dao.delete_dao(model)