from backend.dao.seller_dao import BaseDao
from backend.dao.seller_dao import SellerDao
from backend.models.seller import Seller


def test_instance():
    seller_dao = SellerDao()
    assert isinstance(seller_dao, BaseDao)
    assert isinstance(seller_dao, SellerDao)

def test_dao_save():
    seller_dao = SellerDao()
    seller_model = Seller('Test_Seller', 'Test_Phone', 'Test_Email')
    seller_dao.save(seller_model)
    seller_db = seller_dao.read_all()[-1]
    assert seller_db.name == 'Test_Seller'
    assert seller_db.phone == 'Test_Phone'
    assert seller_db.email == 'Test_Email'

def test_dao_read_all():
    seller_dao = SellerDao()
    seller_db = seller_dao.read_all()
    assert type(seller_db) == list

def test_dao_read_by_id():
    seller_dao = SellerDao()
    seller_db = seller_dao.read_all()[-1]
    seller_by_id = seller_dao.read_by_id(seller_db.id)
    assert seller_db.id == seller_by_id.id

def test_dao_delete():
    seller_dao = SellerDao()
    seller_to_delete = seller_dao.read_all()[-1]
    seller_dao.delete(seller_to_delete)
    seller_db = seller_dao.read_all()[-1]
    assert seller_db.name != 'Test_Seller'
    assert seller_db.phone != 'Test_Phone'
    assert seller_db.email != 'Test_Email'


def run_test_dao():
    try:
        test_instance()
        test_dao_save()
        test_dao_read_all()
        test_dao_read_by_id()
        test_dao_delete()
        print('\033[42;1;30m'+"all dao's tests PASSED"+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+"some test from dao FAILED"+'\033[0;0m')
        raise asserterror
