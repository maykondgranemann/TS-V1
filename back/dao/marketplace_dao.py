from back.models.marketplace_model import Marketplace
from back.dao.base_dao import BaseDao


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)
