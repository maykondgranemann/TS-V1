from backend.dao.seller_dao import SellerDao
from backend.controllers.base_controller import BaseController


class SellerController(BaseController):
    def __init__(self):
        super().__init__(SellerDao)