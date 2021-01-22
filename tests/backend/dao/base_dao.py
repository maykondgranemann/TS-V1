from backend.dao.base_dao import BaseDao
from backend.models.seller_model import Seller

base_dao = BaseDao(Seller)
assert isinstance(base_dao, BaseDao)

result_read_all = base_dao.read_all()
assert isinstance(result_read_all, list)

result_read_by_id = base_dao.read_by_id(1)
assert isinstance(result_read_by_id, Seller)
assert result_read_by_id.id == 1

name = 'Selle_Thiago'
phone = '1591234523'
email = 'seller_thiago@teste.com'
seller = Seller(name, phone, email)
base_dao.save(seller)
last_seller = base_dao.read_all()[-1]

assert name == last_seller.name
assert isinstance(last_seller.name, type(name))
assert phone == last_seller.phone
assert isinstance(last_seller.phone, type(phone))
assert email == last_seller.email
assert isinstance(last_seller.email, type(email))

base_dao.delete(last_seller)
seller_deleted = base_dao.read_by_id(last_seller.id)
assert seller_deleted is None
