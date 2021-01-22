from backend.controllers.base_controller import BaseController
from backend.dao.seller_dao import SellerDao
from backend.models.seller_model import Seller

seller_dao = SellerDao()
base_controller = BaseController(seller_dao)
assert isinstance(base_controller, BaseController)

result_read_all = base_controller.read_all()
assert isinstance(result_read_all, list)

result_read_by_id = base_controller.read_by_id(1)
assert isinstance(result_read_by_id, Seller)
assert result_read_by_id.id == 1
