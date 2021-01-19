from app.database.dao import BaseDao
from app.seller.models import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
