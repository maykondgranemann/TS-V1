import sys
sys.path.append('.')

from back.models.seller_model import Seller
from back.controllers.seller_controller import SellerController

nome = 'Lucas'
telefone = '21955544466'
email = 'lucas@olist.com'
seller = Seller(nome, telefone, email)

controller = SellerController()
assert isinstance(controller, SellerController)
try:
    controller.create('seller')
except Exception as e:
    assert isinstance(e, TypeError)

controller.create(seller)
sellers = controller.read_all()
assert isinstance(sellers, list)

ultimo_id = 0
for s in sellers:
    if s.id > ultimo_id:
        ultimo_id = s.id
seller = controller.read_by_id(ultimo_id)

try:
    seller = controller.read_by_id('ultimo_id')
except Exception as e:
    assert isinstance(e, TypeError)

assert isinstance(seller, Seller)
assert seller._id == ultimo_id
assert seller._name == nome
assert seller._phone == telefone
assert seller._mail == email
assert type(seller._id) == type(ultimo_id)
assert type(seller._name) == type(nome)
assert type(seller._phone) == type(telefone)
assert type(seller._mail) == type(email)

novo_nome = 'Bernardo'
novo_telefone = '2197677667776'
novo_email = 'bernardo@olist.com'
seller._name = novo_nome
seller._phone = novo_telefone
seller._mail = novo_email

controller.update(seller)

try:
    controller.update('seller')
except Exception as e:
    assert isinstance(e, TypeError)

seller = controller.read_by_id(ultimo_id)

assert isinstance(seller, Seller)
assert seller._id == ultimo_id
assert seller._name == novo_nome
assert seller._phone == novo_telefone
assert seller._mail == novo_email
assert type(seller._id) == type(ultimo_id)
assert type(seller._name) == type(novo_nome)
assert type(seller._phone) == type(novo_telefone)
assert type(seller._mail) == type(novo_email)

try:
    controller.delete('seller')
except Exception as e:
    assert isinstance(e, TypeError)

controller.delete(seller)
seller = controller.read_by_id(ultimo_id)
assert seller == None
