import sys
sys.path.append('.')

from SellerAlchemy.controllers.seller_controller import SellerController
from SellerAlchemy.models.seller import Seller

seller = SellerController()

#Create
#--------------------------------------------------------------------------------------------
# seller_create = Seller('Thiago', '15997473684', 'thiago.fiorelli@olist.com')

# seller.create(seller_create)

# for row in seller.read_all():
#       print(row.id, row.name, row.phone, row.email)

#Update
#--------------------------------------------------------------------------------------------
# seller_banco = seller.read_by_id(2)
# print(seller_banco.id, seller_banco.name, seller_banco.phone, seller_banco.email)

# seller_banco.name = 'Jota Canutto'
# seller_banco.phone = '997439316'
# seller_banco.email = 'joao.canutto@olist.com'

# seller.update(seller_banco)

# seller_banco = seller.read_by_id(2)

# print(seller_banco.id, seller_banco.name, seller_banco.phone, seller_banco.email)

#List One
#----------------------------------------------------------------------------------------------
# id = 2
# seller_banco = seller.read_by_id(id)
# print(seller_banco.id, seller_banco.name, seller_banco.phone, seller_banco.email)

#List All
#----------------------------------------------------------------------------------------------
# for row in seller.read_all():
#     print(row.id, row.name, row.phone, row.email)

#Delete
#----------------------------------------------------------------------------------------------
# id = 15
# seller_banco = seller.read_by_id(id)
# seller.delete(seller_banco)

# for row in seller.read_all():
#      print(row.id, row.name, row.phone, row.email)