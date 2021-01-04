from .utils import write_to_logs, write_to_txt_store


def create_product(name: str, description: str, price: float):
    write_to_txt_store(f'Name: {name} - Desc: {description} - Price: {price:.2f}', 'products')
    write_to_logs(f'Created Product - {name}')
