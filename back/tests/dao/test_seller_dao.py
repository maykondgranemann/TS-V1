import sys
sys.path.append('.')

from back.dao.seller_dao import SellerDao


class TestSellerDao:
    
    def test_instance(self):
        seller_dao_instance = SellerDao()
        assert isinstance(seller_dao_instance, BaseDao)
