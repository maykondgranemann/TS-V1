from controllers.seller_controller import SellerController
from models.seller import Seller

controller = SellerController()

all_sellers = controller.read_all()

for seller in all_sellers:
    print(seller)

controller.delete()

# seller = Seller('teste', '11111111', 'teste@teste.com')
# controller.save(seller)

# all_sellers = controller.read_all()

# for seller in all_sellers:
#     print(seller)


