from app.back.controllers.base_controller import BaseController
from app.back.dao.category_dao import CategoryDao

class CategoryController(BaseController):

    def __init__(self, name_entity):
        self.name_entity = name_entity
        self.__dao = CategoryDao()
        super().__init__(self.__dao, self.name_entity)

    # def create_category(category: Category) -> None:
    #     super().create(category)
    #     create_log(f"Created category {category.name}")

    # def read_categories() -> list:
    #     result = super().read()
    #     create_log(f"Listing categories")
    #     return result

    # def update_category(category: Category) -> None:
    #     super().update(category)
    #     create_log(f"Updated category {category.name}")

    # def delete_category(id: str):
    #     super().delete(id)
    #     create_log(f"Deleted category {id}")


