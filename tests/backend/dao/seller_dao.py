from backend.models.seller_model import Seller
from backend.dao.base_dao import BaseDao
from backend.dao.seller_dao import SellerDao

seller_dao = SellerDao()
assert isinstance(seller_dao, SellerDao)
assert isinstance(seller_dao, BaseDao)
assert seller_dao._BaseDao__type_model is Seller