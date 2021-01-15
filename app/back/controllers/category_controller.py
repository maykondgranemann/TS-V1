from app.back.controllers.base_controller import BaseController
from app.back.dao.category_dao import CategoryDao

class CategoryController(BaseController):
    def __init__(self, name_entity):
        self.name_entity = name_entity
        self.__dao = CategoryDao()
        super().__init__(self.__dao, self.name_entity)
