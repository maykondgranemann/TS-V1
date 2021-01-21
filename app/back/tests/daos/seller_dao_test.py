from app.back.dao.base_dao import BaseDao
from app.back.dao.sellers_dao import SellerDao

dao = SellerDao()

assert isinstance(dao, SellerDao)
assert isinstance(dao, BaseDao)
assert dao.entity() == "Seller"