import sys
sys.path.append('.')

from back.dao.seller_dao import SellerDao
from back.dao.base_dao import BaseDao


class TestSellerDao:
    
    def test_instance(self):
        seller_dao_instance = SellerDao()
        assert isinstance(seller_dao_instance, BaseDao)

def start_test_seller_dao():
    test_seller_dao = TestSellerDao()
    test_seller_dao.test_instance()
