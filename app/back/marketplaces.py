from .utils import write_to_logs, write_to_txt_store


def create_marketplace(name: str, description: str):
    write_to_txt_store(f'Name: {name} - Desc: {description}', 'marketplaces')
    write_to_logs(f'Created Marketplace - {name}')
