from pathlib import Path
from app.back.controllers.log_controller import create_log


_file = 'app/back/dao_txt/data/categories.txt'

def set_category(name: str, description: str) -> None:
    file_path = Path(_file)
    if file_path.is_file():
        file = open(_file, "a")
    else:
        file = open(_file, "x")
    file.write(f'{name};{description}\n')

def get_categories() -> list:
    path = Path(_file)
    categories_list = []
    if path.is_file():
        file = open(_file, 'r')
        for line in file:
            categories_list.append(line.strip().split(';'))
        file.close()
    return categories_list