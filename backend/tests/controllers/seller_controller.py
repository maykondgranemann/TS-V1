import sys
sys.path.append('.')

from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller

seller_controller = SellerController()
assert isinstance(seller_controller, SellerController)

# test controller create
seller = Seller('Fulano', '123456', 'fulano@f.com')
seller_controller.create(seller)
assert seller_controller.read_all()[-1].name == 'Fulano'

# test controller read all
assert type(seller_controller.read_all()) == list

# test controller read by id
seller_id = seller_controller.read_all()[0].id
assert isinstance(seller_controller.read_by_id(seller_id), Seller)

# test controller update
seller = seller_controller.read_by_id(seller_id)
seller.name = 'Ciclano'
seller_controller.update(seller)
assert seller_controller.read_by_id(seller_id).name == 'Ciclano'

# test controler delete
seller_controller.delete(seller_controller.read_by_id(seller_id))
for seller in seller_controller.read_all():
    assert seller.id != seller_id
