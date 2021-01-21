import sys
sys.path.append('.')

from backend.daos.seller_dao import SellerDao
from backend.models.seller import Seller


seller_dao = SellerDao()
assert isinstance(seller_dao, SellerDao)

# test DAO save
seller = Seller('Fulano', '123456', 'fulano@f.com')
seller_dao.save(seller)
assert seller_dao.read_all()[-1].name == 'Fulano'

# test DAO read all
assert type(seller_dao.read_all()) == list

# test DAO read by id
seller_id = seller_dao.read_all()[0].id
assert isinstance(seller_dao.read_by_id(seller_id), Seller)

# test DAO delete
seller_dao.delete(seller_dao.read_by_id(seller_id))
for seller in seller_dao.read_all():
    assert seller.id != seller_id