import sys
sys.path.append('.')
from backend.dao.base_dao import BaseDao
from backend.models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self)-> None:
        super().__init__(Seller)
