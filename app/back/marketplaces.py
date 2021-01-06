from .utils import write_to_logs, write_to_txt_store, read_txt


def create_marketplace(name: str, description: str):
    write_to_txt_store(f'Name: {name} - Desc: {description}', 'marketplaces')
    write_to_logs(f'Created Marketplace - {name}')

def read_marketplaces() -> list:
    list_marketplaces = read_txt('marketplaces')
    list_formatted = []
    for line in list_marketplaces:
        marketplace = []
        lista_dados_linha = line.split('-')
        name = lista_dados_linha[0].strip('Name: ')
        descr = lista_dados_linha[1].strip('Desc: ')
        marketplace.append(name)
        marketplace.append(descr)
        list_formatted.append(marketplace)
    write_to_logs('List Marketplaces')
    return list_formatted