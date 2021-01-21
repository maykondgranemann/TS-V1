import sys
sys.path.append('/TS-V1/')

from controller.seller import SellerController
from models.seller import Seller

seller = Seller('Fernanda', 'Fer@olist.com', '34-544323567')

# criação
# SellerController().save(seller)

# leitura
sellers = SellerController().read_all()
for se in sellers:
    print(se.name)

# delete
#SellerController().delete(sellers[0])

# teste update
sellers[0].name = 'Clara'
sellers[0].email = 'clara@olist.com'
SellerController().save(sellers[0])

sellerrs = SellerController().read_all()
for se in sellerrs:
    print(se.name)