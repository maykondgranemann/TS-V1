import sys
sys.path.append('')
from sqlalchemy.orm import sessionmaker
from model.seller_model import Seller
from dao.base_dao import BaseDao

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)


#Testes#
if SellerDao == BaseDao:
    try:
        print('Ok')
    except Exception as e:
        assert isinstance(e, ValueError)
    
