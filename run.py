from controller.controller_seller import SellerController
from model.model_seller import Seller


seller = Seller('Por Deus seller', 'contato@pordeus.com', '11999999999')

SellerController().save(seller)

for s in SellerController().read_all():
    print(s.id, s.name, s.email, s.phone)
