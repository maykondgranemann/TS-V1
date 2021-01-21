from app.back.models.sellers_model import Seller
from app.back.models.base_model import BaseModel

name = "Matheus"
email = "matheus.bachiste@xuribiba.com"
phone = "41970707070"

model = Seller(name, phone, email)

assert isinstance(model, Seller)
assert isinstance(model, BaseModel)
assert model.name == name
assert model.phone == phone
assert model.email == email
assert model.__tablename__ == 'sellers'
