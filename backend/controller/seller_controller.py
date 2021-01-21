import sys
sys.path.append('.')

from backend.dao.seller_dao import SellerDao
from backend.controller.base_controller import BaseController


class SellerController(BaseController):
    def __init__(self) -> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)