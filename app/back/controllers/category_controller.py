from app.back.dao_txt.category_dao_txt import set_category, get_categories
from app.back.controllers.log_controller import create_log


def create_category(name: str, description: str) -> None:
    set_category(name, description)
    create_log(f"Created category {name}")

def read_categories() -> list:
    create_log(f"Listing categories")
    return get_categories()