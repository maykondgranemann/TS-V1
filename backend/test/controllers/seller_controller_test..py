from backend.controllers.seller_controller import SellerController


def start_test_seller_controller():
    tsc = TestSellerController()
    tsc.test_controller()


class TestSellerController:
    def test_controller(self):
        controller_test = SellerController()
        assert isinstance(controller_test, SellerController)
