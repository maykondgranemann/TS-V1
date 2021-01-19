from controller import SellerController
from model import Seller


controller = SellerController()

seller = Seller('Thiago', '1599992233', 'thiago@email.com')
print(seller)

# db_seller = controller.read_by_id(12)
# print(db_seller, '\n')

# db_seller.name = 'Thiago_update'
# db_seller.phone = '1599992222'
# db_seller.email = 'thiago_update@email.com'
# print(db_seller, '\n')

# controller.save(seller)

# controller.delete(12)

sellers_list = controller.read_all()
for item in sellers_list:
    print(item)
