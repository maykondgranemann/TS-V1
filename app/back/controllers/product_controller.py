from app.back.dao.product_dao import ProductDao
from app.back.controllers.base_controller import BaseController

class ProductController(BaseController):
    def __init__(self, name_entity) -> None:
        self.name_entity = name_entity
        self.__dao = ProductDao()
        super().__init__(self.__dao, self.name_entity)



# def create_product(product: Product) -> None:
#     set_product(product)
#     create_log(f"Created product {product.name}")

# def read_products() -> list:
#     products = get_products()
#     create_log(f"Listing products")
#     return products


# def update_product(product: Product) -> None:
#     upd_product(product)
#     create_log(f"Updated product")

# def delete_product(id: str)-> None:
#     del_product(id)
#     create_log(f"Deleted product")