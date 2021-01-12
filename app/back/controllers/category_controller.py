from app.back.dao.category_dao import set_category, get_categories
from app.back.controllers.log_controller import create_log
from app.back.models.category import Category

def create_category(category: Category) -> None:
    set_category(category)
    create_log(f"Created category {category.name}")


def read_categories() -> list:
    categories = get_categories()    
    create_log(f"Listing categories")
    return categories