from models.seller import Seller
from dao.base_dao import BaseDao


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)


# s1 = Seller('Novo nome', '4199933366', 'email@teste.com')
# SellerDao().save(s1)

s4 = SellerDao().read_by_id(4)
print(s4.id, s4.name)
s4.name = 'Jeff'
SellerDao().save(s4)

for s in SellerDao().read_all():
    print(s.name, s.phone, s.email, s.id)