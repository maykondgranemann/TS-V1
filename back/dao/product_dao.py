from back.models.product_model import Product
from back.dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
