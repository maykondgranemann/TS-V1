_file_name = 'app/back/dao_txt/data/products.txt'

def set_product(name: str, description: str, price: float) -> None:
    with open(_file_name, "a") as file:
        file.write(f'{name};{description};{price}\n')
    

def get_products() -> list:
    products_list = []

    with open(_file_name, "r") as file:
        for line in file:
            l = line.strip().split(';')
            l[2] = float(l[2])
            products_list.append(l)

        return products_list