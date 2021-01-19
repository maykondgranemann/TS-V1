import sys
sys.path.append('/teste/')

from dao.base import BaseDao
from models.seller import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)