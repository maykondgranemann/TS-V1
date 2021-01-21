import sys
sys.path.append('.')

from back.models.seller_model import Seller


nome = 'Lucas'
telefone = '21955544466'
email = 'lucas@olist.com'
seller = Seller(nome, telefone, email)

assert isinstance(seller, Seller)
assert seller._name is nome
assert seller._phone is telefone
assert seller._mail is email

try:
    seller._name = seller
except Exception as e:
    assert isinstance(e, TypeError)

try:
    seller._phone = seller
except Exception as e:
    assert isinstance(e, TypeError)

try:
    seller._mail = seller
except Exception as e:
    assert isinstance(e, TypeError)