from back.dao.category_dao import CategoryDao
from back.controllers.base_controller import BaseController

class CategoryController(BaseController):
    def __init__(self):
        super().__init__(CategoryDao)
