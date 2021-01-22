import sys
sys.path.append('.')

from backend.dao.seller_dao import SellerDao
from backend.dao.base_dao import BaseDao


def test_seller_dao():
    dao = SellerDao()
    
    assert isinstance(dao, SellerDao)
    assert isinstance(dao, BaseDao)
    
#test_seller_dao()    