import sys
sys.path.append('.')
from model.seller_model import Seller
from dao.base_dao import BaseDao


class SellerDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Seller)


# TEST-SAVE
# name_ = 'Lucas do Teste'
# phone_ = '(55)+41 99798-9897'
# email_ = 'email@email.com'
# obj_seller = Seller(name_, phone_, email_)
# SellerDao().save(obj_seller)

##TEST-LIST ALL##
# for item in SellerDao().read_all():
#     print(item.id, item.name, item.phone, item.email)

# TEST-LIST BY ID
# result = SellerDao().read_by_id(13)
# print(result.name,result.email)

# TEST-UPDATE
# result = SellerDao().read_by_id(13)
# result.name = 'Lucas Teste'
# result.email = 'lucasteste@teste.com'
# SellerDao().save(result)
# result = SellerDao().read_by_id(13)
# print(result.name,result.email)

# TEST-DELETE
# result = SellerDao().read_by_id(22)
# SellerDao().delete(result)
