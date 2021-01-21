import sys
sys.path.append('.')

from backend.dao.sellers_dao import SellerDao
from backend.controller.base_controller import BaseController


class SellerController(BaseController):
    def __init__(self):
        super().__init__(SellerDao)