from .base_controller import BaseController
from backend.dao.seller_dao import SellerDao


class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)
