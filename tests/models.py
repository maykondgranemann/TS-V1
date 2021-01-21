import sys
sys.path.append('/TS-V1/')

from models.base import BaseModel
from models.seller import Seller

# Base Model
base = BaseModel()
base.identifier = 10

assert base.identifier == 10
assert isinstance(base.identifier, int)

# Seller
seller = Seller()
seller.name = 'Clara'
seller.email = 'clara@olist.com'
seller.phone = '(47) 9 9534-5364'

assert seller.name == 'Clara'
assert isinstance(seller.name, str)
assert seller.email == 'clara@olist.com'
assert isinstance(seller.email, str)
assert seller.phone == '(47) 9 9534-5364'
assert isinstance(seller.phone, str)
