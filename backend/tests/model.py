from backend.models.base_model import BaseModel
from backend.models.seller import Seller
from backend.controllers.seller_controller import SellerController

name = 'Josué Ávila'
email = 'josue.avila@olist.com'
phone = '41997879889'
seller = Seller(name, phone, email)
CONTROLLER = SellerController()

model = BaseModel()
assert model.__abstract__

assert isinstance(seller, Seller)

# Testing get and set from name attribute
assert seller.fullname == name
assert type(name) == type(seller.fullname)
assert isinstance(seller.fullname, str)
assert seller.fullname is name

# Testing get and set from email attribute
assert seller.email == email
assert type(email) == type(seller.email)
assert isinstance(seller.email, str)
assert seller.email is email

# Testing get and set from email attribute
assert seller.phone == phone
assert type(phone) == type(seller.phone)
assert isinstance(seller.email, str)
assert seller.phone is phone

# Test exceptions
try:
    new_test_name = None
    seller.fullname = new_test_name
except Exception as e:
    assert isinstance(e, TypeError)

try:
    new_test_email = None
    seller.email = new_test_email
except Exception as e:
    assert isinstance(e, ValueError)

try:
    new_test_phone = None
    seller.phone = new_test_phone
except Exception as e:
    assert isinstance(e, TypeError)

try:
    new_test_email = 1
    seller.email = new_test_email
except Exception as e:
    assert isinstance(e, ValueError)
