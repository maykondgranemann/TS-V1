from app.back.dao.seller_dao import set_seller, get_seller
from app.back.controllers.log_controller import create_log


def create_seller(name: str, phone: str, mail: str) -> None:
    set_seller(name, phone, mail)
    create_log(f"Created marketplace {name}")

def read_seller() -> list:
    sellers = get_seller()
    create_log(f"Listing marketplaces")
    return sellers
