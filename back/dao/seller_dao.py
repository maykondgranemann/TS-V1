import sys
sys.path.append('.')

from sqlalchemy.orm import sessionmaker
from back.dao.base_dao import BaseDao
from back.models.seller import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

teste = Seller('Antonio', '7616652124', 'antonio@gmail.com')
print(teste)

SellerDao().save(teste)

for sellers in SellerDao().read_all():
    print(sellers.id, sellers.name, sellers.phone, sellers.email)