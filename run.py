from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller


# -- NEW SELLER --
# new_seller = Seller('Name', 'Phone', 'Email')
# SellerController().save(new_seller)

# -- UPDATE SELLER --
# seller = SellerController().read_by_id(40)
# seller.name = 'Marcos'
# seller.phone = '(41) 98888-7777'
# seller.email = 'contato@olist.com'
# SellerController().save(seller)

# -- DELETE SELLER --
# seller = SellerController().read_by_id(40)
# SellerController().delete(seller)

# -- READ BY ID --
# seller = SellerController().read_by_id(1)
# print(seller.name, seller.phone, seller.email)

# -- READ ALL --
# sellers = SellerController().read_all()
# for seller in sellers:
#     print(seller.id, seller.name, seller.phone, seller.email)
