from back.dao.marketplace_dao import MarketplaceDao
from back.controllers.base_controller import BaseController

class MarketplaceController(BaseController):
    def __init__(self):
        super().__init__(MarketplaceDao)
