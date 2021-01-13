_file_name = 'app/back/dao_txt/data/sellers.txt'


def set_seller(name: str, phone: str, mail: str) -> None:
    with open(_file_name, 'a') as file:
        file.write(f'{name};{phone};{mail}\n')
    

def get_seller() -> list:
    list_sellers = []
    with open(_file_name, 'r') as file:
        for line in file:
            treated_line = line.strip().split(';')
            list_sellers.append(treated_line)
        return list_sellers
