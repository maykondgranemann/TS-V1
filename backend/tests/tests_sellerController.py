import sys
sys.path.append('.')
from backend.controllers.seller import SellerController
from backend.dao.base_dao import BaseDao

#Testando se a dao passada na controller é filha de BaseDao
try:
    controller = SellerController()
except Exception as e:
    assert isinstance(e, TypeError)