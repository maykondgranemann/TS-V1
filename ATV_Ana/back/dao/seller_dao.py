from ATV_Ana.back.dao.base_dao import BaseDao
from ATV_Ana.back.models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

