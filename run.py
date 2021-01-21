from controller.seller_controller import SellerController

for item in SellerController().read_all():
    print(item.id, item.name, item.phone, item.email)
