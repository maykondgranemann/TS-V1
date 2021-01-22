from backend.models.seller_model import Seller
from backend.dao.seller_dao import SellerDao
from backend.controllers.base_controller import BaseController
from backend.controllers.seller_controller import SellerController

seller_controller = SellerController()
assert isinstance(seller_controller, SellerController)
assert isinstance(seller_controller, BaseController)

