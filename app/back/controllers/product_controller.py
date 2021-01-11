from app.back.dao.product_dao import set_product, get_products # pega do txt
from app.back.controllers.log_controller import create_log


def create_product(name: str, description: str, price: float) -> None:
    set_product(name, description, price)
    create_log(f"Created product {name}")

def read_products() -> list:
    create_log(f"Listing products")
    return get_products()