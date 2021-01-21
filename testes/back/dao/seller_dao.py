import sys
sys.path.append('.')

from sqlalchemy.orm import sessionmaker
from back.dao.base_dao import BaseDao
from back.models.seller import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

