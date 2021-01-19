import sys
sys.path.append('.')

from controller.seller_controller import SellerController
from models.seller_model import Seller

seller = Seller('Ada', 'a@a.com', '11-111111')

# create/update
# SellerController().save(seller)

# read all
sellers = SellerController().read_all()
for seller in sellers:
    print(seller.name)

# delete
#SellerController().delete(sellers[1])




