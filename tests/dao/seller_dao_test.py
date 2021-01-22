import sys


sys.path.append('.')

from dao.seller_dao import SellerDao
from dao.base_dao import BaseDao
from models.seller import Seller

seller_dao = SellerDao()
assert isinstance(seller_dao, SellerDao)
assert isinstance(seller_dao, BaseDao)