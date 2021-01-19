from backend.models.seller import Seller
from backend.dao.base_dao import BaseDao


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
