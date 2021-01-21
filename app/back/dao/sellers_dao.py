from .base_dao import BaseDao
from ..models.sellers_model import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

    def entity(self):
        return f'Seller'

