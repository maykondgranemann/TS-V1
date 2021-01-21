import sys
sys.path.append('.')

from models.seller import Seller

#Testanto se o objeto é do tipo esperado
name = "Lucas Torres"
telephone = "41997536991"
email = "lucas.torres@olist.com"
seller = Seller(name, telephone, email)

assert type(seller) == Seller
