import sys
sys.path.append('.')
from dao.base_dao import BaseDao
from models.seller import Seller


class SellerDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Seller)


"""
#Insert
seller = Seller('Lucas Torres', '41997536991', 'lucas.torres@olist.com')
SellerDao().insert(seller)

#update
seller = SellerDao().read_by_id(10)
seller.name = 'teste'
SellerDao().insert(seller)

#read by id
seller = SellerDao().read_by_id(10)
print(seller.id, seller.name, seller.telephone, seller.email)

#delete
seller = SellerDao().read_by_id(1)
SellerDao().delete(seller)

#read_all
for seller in SellerDao().read_all():
    print(seller.id, seller.name, seller.telephone, seller.email)

"""