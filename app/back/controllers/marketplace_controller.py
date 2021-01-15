from app.back.controllers.base_controller import BaseController
# from app.back.controllers.log_controller import create_log
from app.back.dao.marketplace_dao import MarketplaceDao

class MarketplaceController(BaseController):
    def __init__(self, name_entity):
        self.name_entity = name_entity
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao, self.name_entity)
