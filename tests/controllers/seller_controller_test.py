import sys

sys.path.append('.')

from controllers.base_controller import BaseController
from controllers.seller_controller import SellerController
from models.seller import Seller


controller = SellerController()
assert isinstance(controller, SellerController)
assert isinstance(controller, BaseController)

