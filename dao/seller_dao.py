from models.seller import Seller
from .base_dao import BaseDao


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)


for s in SellerDao().read_all():
    print(s)