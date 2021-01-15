from app.back.controllers.base_controller import BaseController
# from app.back.controllers.log_controller import create_log
from app.back.dao.marketplace_dao import MarketplaceDao

class MarketplaceController(BaseController):

    def __init__(self, name_entity):
        self.name_entity = name_entity
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao, self.name_entity)

# def create_marketplace(marketplace: Marketplace) -> None:
#     set_marketplace(marketplace)
#     create_log(f"Created marketplace {marketplace.name}")

# def read_marketplace() -> list:
#     marketplaces = get_marketplace()
#     create_log(f"Listing marketplaces")
#     return marketplaces

# def delete_marketplace(id: str):
#     del_marketplace(id)
#     create_log(f"Deleting marketplace")

# def update_marketplace(marketplace: Marketplace):
#     upd_marketplace(marketplace)
#     create_log(f"Deleting marketplaces")
