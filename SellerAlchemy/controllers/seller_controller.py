from SellerAlchemy.dao.seller_dao import SellerDao
from SellerAlchemy.models.seller import Seller

class SellerController():
    def __init__(self):
        self.__dao = SellerDao()

    def create(self, seller: Seller) -> None:
        return self.__dao.save(seller)

    def read_by_id(self, id: int) -> Seller:
        return self.__dao.read_by_id(id)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def delete(self, id: int) -> None:
        self.__dao.delete(id)

    def update(self, seller: Seller) -> Seller:
        self.__dao.save(seller)
    