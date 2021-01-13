from pathlib import Path
from app.back.controllers.log_controller import create_log


_file_name = 'app/back/dao_txt/data/categories.txt'

def set_category(name: str, description: str) -> None:
    with open(_file_name, 'a') as file:
        file.write(f'{name};{description}\n')

def get_categories() -> list:
    categories_list = []
    
    with open(_file_name, 'r') as file:
        for line in file:
            categories_list.append(line.strip().split(';'))
    return categories_list