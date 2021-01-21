from back.dao.seller_dao import SellerDao
from back.controllers.base_controller import BaseController

class SellerController(BaseController):
    def __init__(self):
        super().__init__(SellerDao)
