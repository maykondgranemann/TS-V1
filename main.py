from backend.controllers.seller_controller import SellerController
from backend.models.seller_model import Seller


controller = SellerController()

# seller = Seller('ThiagoTeste', '1599887766', 'thiagorteste@email.com')
# print(seller)

# db_seller = controller.read_by_id(15)
# print(db_seller, '\n')

# db_seller.name = 'Thiago_update2'
# db_seller.phone = '1599992223'
# db_seller.email = 'thiago_update2@email.com'
# print(db_seller, '\n')

# controller.save(seller)

# controller.delete(15)

sellers_list = controller.read_all()
for item in sellers_list:
    print(item)
