from .utils import write_to_logs, write_to_txt_store, read_txt


def create_category(name: str, description: str):
    write_to_txt_store(f'Name: {name} - Desc: {description}', 'categories')
    write_to_logs(f'Created Category - {name}')


def read_categories() -> list:
    list_categories = read_txt('categories')
    list_formatted = []
    for line in list_categories:
        marketplace = []
        lista_dados_linha = line.split('-')
        name = lista_dados_linha[0].strip('Name: ')
        descr = lista_dados_linha[1].strip('Desc: ')
        marketplace.append(name)
        marketplace.append(descr)
        list_formatted.append(marketplace)
    write_to_logs('List Categories')
    return list_formatted
