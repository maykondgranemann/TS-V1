from pathlib import Path


_file_name = 'app/back/dao_txt/data/marketplaces.txt'


def set_marketplace(name: str, description: str) -> None:
    file_path = Path(_file_name)
    if file_path.is_file():
        file = open(_file_name, 'a')
    else:
        file = open(_file_name, 'x')
    file.write(f'{name};{description}\n')
    file.close()

def get_marketplace() -> list:
    list_marketplaces = []
    file = open(_file_name, 'r')
    for line in file:
        treated_line = line.strip().split(';')
        list_marketplaces.append(treated_line)
    file.close()
    return list_marketplaces
