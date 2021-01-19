from sqlalchemy.orm import sessionmaker
from dao.base_dao import BaseDao
from model.seller_model import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
    