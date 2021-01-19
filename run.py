from dotenv import load_dotenv
from backend.controllers.seller_controller import SellerController

CONTROLLER = SellerController()


load_dotenv()
result = CONTROLLER.read_all()
for seller in result:
    print(seller.id, seller.fullname, seller.phone, seller.email)

