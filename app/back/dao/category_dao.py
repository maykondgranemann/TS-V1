from app.back.models.category import Category
from .base_dao import BaseDao

class CategoryDao(BaseDao):
    def create(self, model: Category) -> None:
        query = f"INSERT INTO category (name, description) VALUES ('{model.name}', '{model.description}');"
        super().execute(query)

    def read_by_id(self, id: int) -> Category:
        query = f"SELECT name, description, id FROM category WHERE id = {id};"
        result = super().read(query)[0]
        category = Category(result[0], result[1], result[2])
        return category
    
    def read_all(self) -> list:
        query = f"SELECT name, description, id FROM category;"
        result_list = super().read(query)
        categories = []

        for result in result_list:
            category = Category(result[0], result[1], result[2])
            categories.append(category)
        return categories

    def update(self, model: Category) -> None:
        query = f"UPDATE category SET name='{model.name}', description='{model.description}' WHERE id={model.id}"
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM category WHERE id={id}"
        super().execute(query)
