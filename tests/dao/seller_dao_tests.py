import sys
sys.path.append('')
from dao.base_dao import BaseDao
from dao.seller_dao import SellerDao

#Testes#
if SellerDao == BaseDao:
    try:
        print('Ok')
    except Exception as error:
        assert isinstance(error, ValueError)
    
