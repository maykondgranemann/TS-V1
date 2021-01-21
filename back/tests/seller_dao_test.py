import sys
sys.path.append('.')

from back.models.seller_model import Seller
from back.dao.seller_dao import SellerDao


nome = 'Lucas'
telefone = '21955544466'
email = 'lucas@olist.com'
seller = Seller(nome, telefone, email)

dao = SellerDao()
assert isinstance(dao, SellerDao)

dao.save(seller)

try:
    dao.save('seller')
except Exception as e:
    assert isinstance(e, TypeError)

sellers = dao.read_all()
assert isinstance(sellers, list)

ultimo_id = 0
for s in sellers:
    if s.id > ultimo_id:
        ultimo_id = s.id

try:
    dao.read_by_id('seller')
except Exception as e:
    assert isinstance(e, TypeError)

seller = dao.read_by_id(ultimo_id)

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

dao.save(seller)
seller = dao.read_by_id(ultimo_id)

assert isinstance(seller, Seller)
assert seller._id is ultimo_id
assert seller._name == novo_nome
assert seller._phone == novo_telefone
assert seller._mail == novo_email
assert type(seller._id) == type(ultimo_id)
assert type(seller._name) == type(novo_nome)
assert type(seller._phone) == type(novo_telefone)
assert type(seller._mail) == type(novo_email)

try:
    dao.delete('seller')
except Exception as e:
    assert isinstance(e, TypeError)

dao.delete(seller)
seller = dao.read_by_id(ultimo_id)
assert seller == None


#

