import sys
sys.path.append('.')

from backend.controller.seller_controller import SellerController
from backend.controller.base_controller import BaseController


def test_seller_controller():
    seller_controller = SellerController()
    
    assert isinstance(seller_controller, SellerController)
    assert isinstance(seller_controller, BaseController)
    
#test_seller_controller()    