from back.dao.base_dao import BaseDao
from back.models.seller import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
