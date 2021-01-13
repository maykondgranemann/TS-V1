_file_name = 'app/back/dao_txt/data/marketplaces.txt'


def set_marketplace(name: str, description: str) -> None:
    with open(_file_name, 'a') as file:
        file.write(f'{name};{description}\n')


def get_marketplace() -> list:
    list_marketplaces = []
    with open(_file_name, 'r') as file:
        for line in file:
            treated_line = line.strip().split(';')
            list_marketplaces.append(treated_line)
        return list_marketplaces
