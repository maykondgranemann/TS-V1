from controller.seller_controller import SellerController
from model.seller_model import Seller

seller = Seller('agora foi', '28 99999-9999', 'agrfoi@carrefour.com')
SellerController().save(seller)

for s in SellerController().read_all():
    print(s.id, s.name, s.phone, s.email)