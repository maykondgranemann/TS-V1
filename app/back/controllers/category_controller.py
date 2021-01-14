from app.back.dao.category_dao import set_category, get_categories, upd_category, del_category
from app.back.controllers.log_controller import create_log
from app.back.models.category import Category

def create_category(category: Category) -> None:
    set_category(category)
    create_log(f"Created category {category.name}")


def read_categories() -> list:
    categories = get_categories()    
    create_log(f"Listing categories")
    return categories


def update_category(category: Category) -> None:
    upd_category(category)
    create_log(f"Updated category {category.name}")


def delete_category(id: str):
    del_category(id)
    create_log(f"Deleted category {id}")