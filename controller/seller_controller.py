from controller.base_controller import BaseController
from dao.seller_dao import SellerDao


class SellerController(BaseController):
    def __init__(self) -> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)
