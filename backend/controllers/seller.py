from backend.controllers.base_controller import BaseController
from backend.dao.seller import SellerDao


class SellerController(BaseController):
    def __init__(self):
        dao = SellerDao()
        super().__init__(dao)


