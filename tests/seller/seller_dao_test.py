import sys
sys.path.append('.')

from dao.seller_dao import SellerDao
from models.seller import Seller

#Test insert
seller = Seller('Test Dao', '411111111', 'testdao@olist.com')
result = SellerDao().save(seller)
seller = SellerDao().read_by_id(result)

assert seller.name == 'Test Dao'
assert seller.telephone == '411111111'
assert seller.email == 'testdao@olist.com'

#Read all
list_all = SellerDao().read_all()
assert isinstance(list_all, list)