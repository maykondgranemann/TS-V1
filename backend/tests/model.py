from backend.models.base_model import BaseModel
from backend.models.seller import Seller
from backend.controllers.seller_controller import SellerController
from dotenv import load_dotenv

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

# Testing Base Model
load_dotenv()
result = CONTROLLER.save(seller)
identifier = result[0]
assert isinstance(identifier, int)

# Test exceptions



