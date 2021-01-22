from backend.controllers.seller_controller import BaseController
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller


def test_controller_instance():
    seller = SellerController()
    assert isinstance(seller, BaseController)
    assert isinstance(seller, SellerController)

def test_controller_save():
    seller_controller = SellerController()
    seller_model = Seller('Test_Seller', 'Test_Phone', 'Test_Email')
    seller_controller.save(seller_model)
    seller_db_by_controller = seller_controller.read_all()[-1]
    assert seller_db_by_controller.name == 'Test_Seller'
    assert seller_db_by_controller.phone == 'Test_Phone'
    assert seller_db_by_controller.email == 'Test_Email'

def test_controller_read_all():
    seller_controller = SellerController()
    seller_db_by_controller = seller_controller.read_all()
    assert type(seller_db_by_controller) == list

def test_controller_read_by_id():
    seller_controller = SellerController()
    seller_db_by_controller = seller_controller.read_all()[-1]
    seller_by_id = seller_controller.read_by_id(seller_db_by_controller.id)
    assert seller_db_by_controller.id == seller_by_id.id

def test_controller_delete():
    seller_controller = SellerController()
    seller_to_delete = seller_controller.read_all()[-1]
    seller_controller.delete(seller_to_delete)
    seller_db_by_controller = seller_controller.read_all()[-1]
    assert seller_db_by_controller.name != 'Test_Seller'
    assert seller_db_by_controller.phone != 'Test_Phone'
    assert seller_db_by_controller.email != 'Test_Email'


def run_test_controller():
    try:
        test_controller_instance()
        test_controller_save()
        test_controller_read_all()
        test_controller_read_by_id()
        test_controller_delete()
        print('\033[42;1;30m'+"all controller's tests PASSED"+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+"some test from controller FAILED"+'\033[0;0m')
        raise asserterror
