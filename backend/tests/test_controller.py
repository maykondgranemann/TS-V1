from backend.controllers.seller_controller import BaseController
from backend.controllers.seller_controller import SellerController


def test_controller_instance():
    seller = SellerController()
    assert isinstance(seller, BaseController)
    assert isinstance(seller, SellerController)


def run_test_controller():
    try:
        test_controller_instance()
        print('\033[42;1;30m'+"all controller's tests PASSED"+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+"some test from controller FAILED"+'\033[0;0m')
        raise asserterror
