from ATV_Ana.back.controller.seller_controller import SellerController
from ATV_Ana.back.models.seller import Seller


controller = SellerController()

result = controller.read_all()

assert isinstance(result, list)

sel = result[0]

assert isinstance(sel, Seller)

name = sel.name

new_sell = controller.read_by_id(sel.id)

assert isinstance(new_sell, Seller)

assert new_sell.name == name

new_sell.name = 'Toronto'

controller.create_update(new_sell)

result = controller.read_by_id(sel.id)

assert result.name == 'Toronto'

seller = Seller('Canada', '123465479812', 'teste@canada.com')

controller.create_update(seller)

controller.delete(seller)

result = controller.read_all()

item = None
for i in result:
    if i.phone == '123465479812':
        item = i

assert item is None
