from luciana.controller.controller_seller import SellerController
from luciana.models.seller import Seller

seller = Seller('Luciana', 'a@a.com', '11223344')

SellerController().save(seller)

for a in SellerController().read_all():
    print(a.id, a.nome, a.email, a.telefone)
