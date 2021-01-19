import sys
sys.path.append('/teste/')

from dao.seller import SellerDao
from controller.base import BaseController

class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)