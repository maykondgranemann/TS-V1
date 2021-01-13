from app.back.dao.marketplace_dao import set_marketplace, get_marketplace, upd_marketplace
from app.back.controllers.log_controller import create_log
from app.back.models.marketplace import Marketplace

def create_marketplace(marketplace: Marketplace) -> None:
    set_marketplace(marketplace)
    create_log(f"Created marketplace {marketplace.name}")

def read_marketplace() -> list:
    marketplaces = get_marketplace()
    create_log(f"Listing marketplaces")
    return marketplaces

def delete_marketplace():
    pass

def update_marketplace(marketplace: Marketplace):
    upd_marketplace(marketplace)
