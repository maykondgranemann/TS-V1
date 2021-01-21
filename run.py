from controller.seller_controller import SellerController
from model.seller_model import Seller

seller = Seller('novo seller', 'novo phone', 'novo email')
SellerController().save(seller)

for s in SellerController().read_all():
    print(s.id, s.name, s.phone, s.email)