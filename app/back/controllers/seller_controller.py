from app.back.dao.seller_dao import set_seller, get_seller
from app.back.controllers.log_controller import create_log
from app.back.models.seller import Seller

def create_seller(seller: Seller) -> None:
    set_seller(seller)
    create_log(f"Created seller {seller.name}")

def read_seller() -> list:
    sellers = get_seller()
    create_log(f"Listing sellers")
    return sellers
