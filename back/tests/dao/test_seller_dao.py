import sys
sys.path.append('.')

from back.dao.seller_dao import SellerDao
from back.dao.base_dao import BaseDao
from back.models.seller import Seller


class TestSellerDao:
    
    def test_instance(self):
        seller_dao_instance = SellerDao()
        assert isinstance(seller_dao_instance, BaseDao)
