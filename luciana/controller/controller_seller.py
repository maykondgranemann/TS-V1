from luciana.dao.seller_dao import SellerDao
from luciana.controller.controller_base import BaseController


class SellerController(BaseController):
    def __init__(self):
        super().__init__(SellerDao)