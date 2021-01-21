import sys
sys.path.append('.')

from back.controllers.seller_controller import SellerController


class TestSellerController:
    def test_instance(self):
        test_object  = SellerController()
        assert isinstance(test_object, SellerController)

def begin_seller_controller_tests():
    test_seller_controller = TestSellerController()
    test_seller_controller.test_instance()
