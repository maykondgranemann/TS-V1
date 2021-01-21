import sys
sys.path.append('.')

from backend.models.seller import Seller


seller = Seller('Fulano', '123456', 'fulano@f.com')

assert type(seller) == Seller
assert isinstance(seller, Seller)

assert seller.name == 'Fulano'
assert seller.phone == '123456'
assert seller.email == 'fulano@f.com'

assert type(seller.name) == str
assert type(seller.phone) == str
assert type(seller.email) == str
