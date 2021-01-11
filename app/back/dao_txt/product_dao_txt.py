from pathlib import Path


_file = 'app/back/dao_txt/data/products.txt'

def set_product(name: str, description: str, price: float) -> None:
    file_path = Path(_file)
    if file_path.is_file():
        file = open(_file, "a")
    else:
        file = open(_file, "x")
    file.write(f'{name};{description};{price}\n')
    

def get_products() -> list:
    products_list = []
    path = Path(_file)
    if path.is_file():
        file = open(_file, "r")
        for line in file:
            l = line.strip().split(';')
            l[2] = float(l[2])
            products_list.append(l)
        file.close()
    
    return products_list