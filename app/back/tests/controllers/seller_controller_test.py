from app.back.controllers.seller_controller import SellerController
from app.back.models.sellers_model import Seller


# Dados para teste
name = "Xablau"
phone = "41970707070"
email = "matheus.bachiste@xuribiba.com"
seller = Seller(name, phone, email)
seller_controller = SellerController()

def test_create():
    seller_controller.create(seller)
    seller_db = seller_controller.read_all()[-1]

    assert isinstance(seller_controller, SellerController)
    assert seller_db.name == name
    assert seller_db.phone == phone
    assert seller_db.email == email

def test_read_all():
    sellers_list = seller_controller.read_all()

    assert isinstance(sellers_list, list)

def test_delete():
    seller_controller.create(seller)
    seller_db = seller_controller.read_all()[-1]

    seller_controller.delete(seller_db.id)
    assert seller_controller.read_by_id(seller_db.id) == None