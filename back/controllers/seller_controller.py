import sys
sys.path.append('.')

from back.models.seller_model import Seller
from back.dao.seller_dao import SellerDao


class SellerController():
    def create(self, model: Seller) -> None:
        SellerDao().save(model)
    
    def update(self, model:Seller) -> None:
        SellerDao().save(model)

    def read_by_id(self, id:int) -> Seller:
        seller = SellerDao().read_by_id(id, Seller)
        return seller
    
    def read_all(self) -> list:
        sellers = SellerDao().read_all(Seller)
        return sellers
    
    def delete(self, model: Seller) -> None:
        SellerDao().delete(model)

seller = Seller('Lucas', '219999999999', 'lucas@olist.com')

SellerController().create(seller)

seller = SellerController().read_by_id(23)

seller.name = "Lucas João"

SellerController().update(seller)

seller = SellerController().read_by_id(23)

print(seller)

SellerController().delete(seller)

sellers = SellerController().read_all()

for s in sellers:
    print(s)

