from app.back.dao.product_dao import ProductDao
from app.back.controllers.base_controller import BaseController

class ProductController(BaseController):
    def __init__(self, name_entity) -> None:
        self.name_entity = name_entity
        self.__dao = ProductDao()
        super().__init__(self.__dao, self.name_entity)
