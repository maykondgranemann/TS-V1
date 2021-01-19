from back.models.category_model import Category
from back.dao.base_dao import BaseDao


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
