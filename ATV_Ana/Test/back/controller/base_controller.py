from ATV_Ana.back.dao.seller_dao import SellerDao
from ATV_Ana.back.controller.base_controller import BaseController
from ATV_Ana.back.models.seller import Seller


class Test(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)


test = Test()

result = test.read_all()

assert isinstance(result, list)

item = result[0]

assert isinstance(item, Seller)

id_ = item.id

assert isinstance(test.read_by_id(id_), Seller)

test.create_update(Seller('NOvo', '213434354', 'novo1321670@test.com.br'))

result = test.read_all()

for i in result:
    if i.phone == '213434354':
        item = i

item.name = 'New name oooo'

test.create_update(item)

result = test.read_all()

for i in result:
    if i.phone == '213434354':
        id_ = i.id
        item = i

assert item.name == 'New name oooo'

test.delete(item)

assert test.read_by_id(id_) is None
