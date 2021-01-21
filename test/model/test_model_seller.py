import sys
sys.path.append('.')

from model.model_seller import Seller


name = "B2W"
email = "contato@seller.com"
phone = "(11)9 9999-9999"

seller1 = Seller(name, email, phone)

# Testando objeto da classe Seller
assert isinstance(seller1, Seller)
