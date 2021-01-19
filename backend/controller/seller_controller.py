import sys
sys.path.append('.')

from backend.models.seller import Seller
from backend.dao.seller_dao import SellerDao

class SellerController:
    def save_seller(self, obj: Seller) -> None:
        SellerDao().save(obj)


    def listall(self) -> list:
        list = SellerDao().read_all()
        return list
    
    def read_id(self, id:int):
        result = SellerDao().read_by_id(id)
        return result
        
    def delete_seller(self, obj:Seller):    
        SellerDao().delete(obj)
        

