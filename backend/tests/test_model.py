from backend.models.base_model import BaseModel
from backend.models.seller import Seller


def run_test_model():
    # Test Seller Model
    seller = Seller('Test_Seller', 'Test_Phone', 'Test_Email')

    try:
        assert isinstance(seller, BaseModel)
        assert isinstance(seller, Seller)
        assert seller.name == 'Test_Seller'
        assert seller.phone == 'Test_Phone'
        assert seller.email == 'Test_Email'
        print('\033[42;1;30m'+'all models tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+'some test from model FAILED'+'\033[0;0m')
        raise asserterror
