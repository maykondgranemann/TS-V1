from app.back.controllers.base_controller import BaseController
# from app.back.controllers.log_controller import create_log
from app.back.dao.seller_dao import SellerDao

class SellerController(BaseController):

    def __init__(self, name_entity):
        self.name_entity = name_entity
        self.__dao = SellerDao()
        super().__init__(self.__dao, self.name_entity)

# def create_seller(seller: Seller) -> None:
#     set_seller(seller)
#     create_log(f"Created seller {seller.name}")

# def read_seller() -> list:
#     sellers = get_seller()
#     create_log(f"Listing sellers")
#     return sellers

# def delete_seller(id: str):
#     del_seller(id)
#     create_log(f"Listing sellers")

# def update_seller(seller: Seller):
#     upd_seller(seller)
#     create_log(f"Deleting sellers")