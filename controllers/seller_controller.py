from controllers.base_controller import BaseController
from dao.seller_dao import SellerDao


class SellerController(BaseController):
    def __init__(self):
        dao = SellerDao()
        super().__init__(dao)
