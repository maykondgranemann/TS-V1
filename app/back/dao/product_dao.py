from app.back.models.product import Product
from .base_dao import BaseDao

class ProductDao(BaseDao):
    def create(self, model: Product) -> None:
        query = f"INSERT INTO product (name, description, price) VALUES ('{model.name}', '{model.description}', '{model.price}');"
        super().execute(query)
    
    def read_by_id(self, id: int) -> Product:
        query = f"SELECT name, description, price, id FROM product WHERE id = {id};"
        result = super().read(query)[0]
        product = Product(result[0], result[1], result[2], result[3])
        return product
    
    def read_all(self) -> list:
        query = f"SELECT name, description, price, id FROM product"
        result_list = super().read(query)
        products = []

        for result in result_list:
            product = Product(result[0], result[1], result[2], result[3])
            products.append(product)
        return products

    def update(self, model: Product) -> None:
        query = f"UPDATE product SET name='{model.name}', description='{model.description}', price='{model.price}' WHERE id={model.id}"
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM product WHERE id={id}"
        super().execute(query)
        
