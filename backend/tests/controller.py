from backend.controllers.base_controller import BaseController
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller
from backend.dao.seller_dao import SellerDao
from dotenv import load_dotenv

CONTROLLER_LIST = [SellerController(), BaseController(SellerDao)]

for CONTROLLER in CONTROLLER_LIST:

    name = 'Josué Ávila'
    email = 'josue.avila@olist.com'
    phone = '41997879889'
    seller = Seller(name, phone, email)
    load_dotenv()

    # Testing read_all method
    sellers = CONTROLLER.read_all()
    assert isinstance(sellers, list)
    assert all(isinstance(item, Seller) for item in sellers)

    # Testing insert and read_by_id methods
    result = CONTROLLER.save(seller)
    identifier = result[0]
    state_persistent = result[1]
    saved_seller = CONTROLLER.read_by_id(identifier)
    assert isinstance(saved_seller, Seller)
    assert isinstance(identifier, int)
    assert saved_seller.fullname == name
    assert saved_seller.phone == phone
    assert saved_seller.email == email
    assert state_persistent

    # Testing update and read_by_id methods
    new_name = 'Josué Rosa de Ávila'
    new_email = 'josue.rosadeavila@gmail.com'
    new_phone = '42999437330'

    saved_seller.fullname = new_name
    saved_seller.email = new_email
    saved_seller.phone = new_phone
    result = CONTROLLER.save(saved_seller)
    same_identifier = result[0]
    state_updated = result[1]
    updated_seller = CONTROLLER.read_by_id(same_identifier)

    assert isinstance(updated_seller, Seller)
    assert updated_seller.fullname == new_name
    assert updated_seller.phone == new_phone
    assert updated_seller.email == new_email
    assert state_updated

    # Testing update and read_by_id methods
    seller_to_delete = updated_seller
    state_deleted = CONTROLLER.delete(seller_to_delete)
    assert state_deleted
