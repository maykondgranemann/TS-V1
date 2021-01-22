import sys
sys.path.append('.')

from models.seller import Seller

name = 'João'
email = 'joão@gmail.com'
phone = '41999998888'
seller = Seller(name, email, phone)
assert seller.name == name
assert seller.email == email
assert seller.phone == phone
