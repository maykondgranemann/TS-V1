from back.models.seller_model import Seller
from back.dao.base_dao import BaseDao


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
