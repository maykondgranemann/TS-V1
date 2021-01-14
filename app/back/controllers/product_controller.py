from app.back.dao.product_dao import set_product, get_products, upd_product, del_product # pega do txt
from app.back.controllers.log_controller import create_log
from app.back.models.product import Product


def create_product(product: Product) -> None:
    set_product(product)
    create_log(f"Created product {product.name}")

def read_products() -> list:
    products = get_products()
    create_log(f"Listing products")
    return products


def update_product(product: Product) -> None:
    upd_product(product)
    create_log(f"Updated product")

def delete_product(id: str)-> None:
    del_product(id)
    create_log(f"Deleted product")