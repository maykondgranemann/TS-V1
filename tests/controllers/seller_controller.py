import sys
sys.path.append('.')

from controllers.seller_controller import SellerController
from controllers.base_controller import BaseController
from models.seller import Seller

ctrl = SellerController()

#testar construtor
assert isinstance(ctrl, SellerController)
assert isinstance(ctrl, BaseController)

sel = Seller("Regina", "email@email.com", "67-999271211", 100)

#testar create
ctrl.create(sel)
assert ctrl.read_by_id(100).name == "Regina"
assert ctrl.read_by_id(100).identifier == 100
assert ctrl.read_by_id(100).email == "email@email.com"
assert ctrl.read_by_id(100).phone == "67-999271211"

#testar read all
assert isinstance(ctrl.read_all(), list)

#testar read by id
assert isinstance(ctrl.read_by_id(100), Seller)

#testar update
sel.name = "Regina Beretta"
ctrl.update(sel)
assert ctrl.read_by_id(100).name == "Regina Beretta"

#testar delete
ctrl.delete(ctrl.read_by_id(100))