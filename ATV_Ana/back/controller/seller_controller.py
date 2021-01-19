from ATV_Ana.back.dao.seller_dao import SellerDao
from ATV_Ana.back.controller.base_controller import BaseController


class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)