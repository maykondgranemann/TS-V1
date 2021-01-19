from model.seller_model import Seller
from controller.seller_controller import SellerController

seller = Seller('Quésia Santos', '28 99999-9999', 'quesia@carrefour.com')

seller = SellerController().read_all()
for s in seller:
    print(s.name_seller)

seller[0].name_seller = 'Quesia'
seller[0].email = 'quesia@carrefour.com'
SellerController().create(seller[0])

sellerrs = SellerController().read_all()
for s in seller:
    print(s.name_seller)
