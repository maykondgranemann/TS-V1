from ..controllers.base_controller import BaseController
from ..dao.sellers_dao import SellerDao

class SellerController(BaseController):
    def __init__(self)-> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)
