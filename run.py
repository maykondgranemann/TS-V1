from dotenv import load_dotenv
from backend.controllers.seller_controller import SellerController
from backend.models.seller import SellerModel

CONTROLLER = SellerController()

#seller = SellerModel('Josué Ávila', '41997879889', 'josue.avila@olist.com')
#CONTROLLER.save(seller)

seller = CONTROLLER.read_by_id(9)
seller.fullname = 'Josué Rosa de Ávila'
CONTROLLER.save(seller)

result = CONTROLLER.read_all()
for seller in result:
    print(seller.id, seller.fullname, seller.phone, seller.email)

