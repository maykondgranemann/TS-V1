from ATV_Ana.back.dao.base_dao import BaseDao
from ATV_Ana.back.models.seller import Seller

test = BaseDao(Seller)

result = test.read_all()

assert isinstance(result, list)

sel = Seller('Teste', '1221443254', '12214testvo423o65@help.com')

test.create_update(sel)

result = test.read_all()

for item in result:
    if item.email == '12214testvo423o65@help.com':
        sel = item

assert isinstance(sel.id, int)

assert sel.name == 'Teste'
assert sel.phone == '1221443254'

id_ = sel.id
sel.email = '12214nothingnovo@help.com'

test.create_update(sel)

new_seller = test.read_by_id(id_)

assert new_seller.email == '12214nothingnovo@help.com'

test.delete(new_seller)

result = test.read_by_id(id_)

assert result == None
