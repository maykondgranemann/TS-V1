from back.dao.product_dao import ProductDao
from back.controllers.base_controller import BaseController

class ProductController(BaseController):
    def __init__(self):
        super().__init__(ProductDao)
