from pathlib import Path


_file_name = 'app/back/dao_txt/data/sellers.txt'


def set_seller(name: str, phone: str, mail: str) -> None:
    file_path = Path(_file_name)
    if file_path.is_file():
        file = open(_file_name, 'a')
    else:
        file = open(_file_name, 'x')
    file.write(f'{name};{phone};{mail}\n')
    file.close()

def get_seller() -> list:
    list_sellers = []
    file = open(_file_name, 'r')
    for line in file:
        treated_line = line.strip().split(';')
        list_sellers.append(treated_line)
    file.close()
    return list_sellers
