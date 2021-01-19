import sys
sys.path.append('/teste/')

from controller.seller import SellerController
from models.seller import Seller

seller = Seller('Fernanda', 'Fer@olist.com', '34-544323567')

# criação
# SellerController().create(seller)

# leitura
sellers = SellerController().read_all()
for se in sellers:
    print(se.name_seller)

# delete
#SellerController().delete(sellers[0])

# teste update
sellers[0].name_seller = 'Clara'
sellers[0].email = 'clara@olist.com'
SellerController().create(sellers[0])

sellerrs = SellerController().read_all()
for se in sellerrs:
    print(se.name_seller)