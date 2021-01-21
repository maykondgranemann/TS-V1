from backend.dao.seller_dao import SellerDao
from .base_controller import BaseController

class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)