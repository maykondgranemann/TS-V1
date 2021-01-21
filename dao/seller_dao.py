from dao.base_dao import BaseDao
from models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Seller)
