import sys
sys.path.append('.')

from sqlalchemy.orm import sessionmaker
from luciana.dao.base_dao import BaseDao
from luciana.models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)


sell = Seller('Luciana', 'luciana@olist.com', '11998877663322')

SellerDao().save(sell)

for s in SellerDao().read_all():
    print(s.id, s.nome, s.email, s.telefone)