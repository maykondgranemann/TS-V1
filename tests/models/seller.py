import sys
sys.path.append('.')

from models.base_model import BaseModel
from models.seller import Seller

identifier = 10
nome = "Regina"
email = "regina@olist.com"
phone = "67-999271211"
sel1 = Seller(nome, email, phone, identifier)

#testando construtor
assert isinstance(sel1, Seller)
assert isinstance(sel1, BaseModel)

#testando atribuições name_seller
assert sel1.name == nome
assert type(nome) == type(sel1.name)
assert isinstance(sel1.name, str)

#testando atribuições email
assert sel1.email == email
assert type(sel1.email) == type(email)
assert isinstance(sel1.email, str)

#testando atribuições phone
assert sel1.phone == phone
assert type(sel1.phone) == type(phone)
assert isinstance(sel1.phone, str)

#testando atribuições id
assert sel1.identifier == identifier
assert type(sel1.identifier) == type(identifier)
assert isinstance(sel1.identifier, int)
