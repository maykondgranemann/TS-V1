import sys
sys.path.append('.')

from luciana.dao.base_dao import BaseDao
from luciana.dao.seller_dao import SellerDao

#Testes#
if SellerDao == BaseDao:
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, ValueError)