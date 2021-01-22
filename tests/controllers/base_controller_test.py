import sys

sys.path.append('.')

from models.seller import Seller
from dao.base_dao import BaseDao
from controllers.base_controller import BaseController


base_dao = BaseDao(Seller)
controller = BaseController(base_dao)
assert isinstance(controller, BaseController)