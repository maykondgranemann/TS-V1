from backend.dao.seller_dao import SellerDao


class SellerController:
    def __init__(self):
        self.dao = SellerDao()

    def save(self, model: object) -> None:
        self.dao.save(model)

    def read_all(self) -> list:
        result = self.dao.read_all()
        return result

    def read_by_id(self, id: int) -> object:
        result = self.dao.read_by_id(id)
        return result

    def delete(self, model: object) -> None:
        self.dao.delete(model)
