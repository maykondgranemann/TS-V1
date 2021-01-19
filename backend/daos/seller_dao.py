from backend.daos.base_dao import BaseDao
from backend.models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
