from .utils import write_to_logs, write_to_txt_store, read_txt
import re

def create_product(name: str, description: str, price: float):
    write_to_txt_store(f'Name: {name} - Desc: {description} - Price: {price:.2f}', 'products')
    write_to_logs(f'Created Product - {name}')

def read_products()-> list:
    list_products = read_txt('products')
    
    for i, line in enumerate(list_products):
        str_ = re.search("Name: (.+?) - Desc: (.+?) - Price: (.+?)", line)
        result = {
            "name":str_.group(1),
            "description":str_.group(2),
            "price":float(str_.group(3))
        }
        list_products[i] = result
    return list_products
        