from app.back.dao.marketplace_dao import set_marketplace, get_marketplace
from app.back.controllers.log_controller import create_log


def create_marketplace(name: str, description: str) -> None:
    set_marketplace(name, description)
    create_log(f"Created marketplace {name}")

def read_marketplace() -> list:
    marketplaces = get_marketplace()
    create_log(f"Listing marketplaces")
    return marketplaces
