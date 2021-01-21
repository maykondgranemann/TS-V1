from ..controllers.base_controller import BaseController
from ..dao.sellers_dao import SellerDao

class SellerController(BaseController):
    def __init__(self, name_entity):
        self.name_entity = name_entity
        self.__dao = SellerDao()
        super().__init__(self.__dao, self.name_entity)
