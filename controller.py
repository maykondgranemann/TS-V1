from model import Seller
from dao import SellerDao


class SellerController:
    def __init__(self):
        self.__dao = SellerDao()

    def save(self, model: Seller) -> None:
        self.__dao.save(model)

    def read_by_id(self, id: int) -> Seller:
        return self.__dao.read_by_id(id)

    def read_all(self) -> list[Seller]:
        return self.__dao.read_all()

    def delete(self, id: int) -> None:
        model = self.__dao.read_by_id(id)
        self.__dao.delete(model)
    