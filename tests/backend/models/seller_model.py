from backend.models.seller_model import Seller
from backend.models.base_model import BaseModel

name = 'Thiago'
phone = '15991111111'
email = 'thiago@teste.com'

seller = Seller(name, phone, email)

assert isinstance(seller, BaseModel)
assert isinstance(seller, Seller)
assert hasattr(seller, 'name')
assert hasattr(seller, 'phone')
assert hasattr(seller, 'email')
assert seller.__tablename__ == 'sellers'
assert seller.name is name
assert seller.phone is phone
assert seller.email is email


