from controllers.base_controller import BaseController
from dao.seller_dao import SellerDao
from models.seller import Seller


class SellerController(BaseController):
    def __init__(self) -> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)



"""
#Insert
seller = Seller('Lucas Torres', '41997536991', 'lucas.torres@olist.com')
SellerController().save(seller)

#update
seller = SellerDao().read_by_id(10)
seller.name = 'teste'
SellerDao().save(seller)

#read by id
seller = SellerDao().read_by_id(10)
print(seller.id, seller.name, seller.telephone, seller.email)

#delete
seller = SellerDao().read_by_id(1)
SellerDao().delete(seller)


#read_all
for seller in SellerController().read_all():
    print(seller.id, seller.name, seller.telephone, seller.email)
"""