import sys
sys.path.append('/TS-V1/')

from dao.base import BaseDao
from models.seller import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)