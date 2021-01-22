from ATV_Ana.back.dao.seller_dao import SellerDao
from ATV_Ana.back.models.seller import Seller

dao = SellerDao()


result = dao.read_all()

assert isinstance(result, list)

sel = Seller('Teste Dao Seller', '1221443254', 'testeDao@help.com')

dao.create_update(sel)

result = dao.read_all()

for item in result:
    if item.email == 'testeDao@help.com':
        sel = item

assert isinstance(sel.id, int)

assert sel.name == 'Teste Dao Seller'
assert sel.phone == '1221443254'

id_ = sel.id
sel.email = 'testeDaoUpdate@help.com'

dao.create_update(sel)

new_seller = dao.read_by_id(id_)

assert new_seller.email == 'testeDaoUpdate@help.com'

dao.delete(new_seller)

result = dao.read_by_id(id_)

assert result == None