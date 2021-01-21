from dao.dao_seller import SellerDao
from controller.controller_base import BaseController


class SellerController(BaseController):
    def __init__(self):
        super().__init__(SellerDao)
