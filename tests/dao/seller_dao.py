import sys
sys.path.append('.')

from dao.seller_dao import SellerDao
from dao.base_dao import BaseDao
from models.seller import Seller
from models.base_model import BaseModel

dao = SellerDao()

#testar construtor
assert isinstance(dao, BaseDao)
assert isinstance(dao, SellerDao)

sel = Seller("Regina", "regina@olist.com", "67-999271211", 10)

#testar save
assert dao.save(sel) == None
assert isinstance(dao.read_by_id(10),BaseModel)
assert isinstance(dao.read_by_id(10),Seller)

#testar read all
assert isinstance(dao.read_all() ,list)

#testar read by id
assert isinstance(dao.read_by_id(10), Seller)

#testar delete
assert dao.delete(dao.read_by_id(10)) == None
assert dao.read_by_id(10) == None

