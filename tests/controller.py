import sys
sys.path.append('/TS-V1/')

from models.seller import Seller
from controller.base import BaseController
from controller.seller import SellerController

# Base Controller
base = BaseController()
base.identifier = 10

assert base.identifier == 10
assert isinstance(base.identifier, int)

# Seller
seller = Seller()
seller.name = 'Clara'
seller.email = 'clara@olist.com'
seller.phone = '(47) 9 9534-5364'
SellerController().save(seller)

sellers = SellerController().read_all()
assert SellerController().read_all() == None
assert isinstance(sellers, list)

assert SellerController().read_by_id(0) == None
sel = SellerController().read_by_id(0)

sel.name = 'Cla'
assert SellerController().save(sel) == None
assert isinstance(sellers, list)

assert SellerController().delete(seller) == None

