import sys
sys.path.append('.')

from back.controllers.tests_controller import start_tests

def menu():
    options = ['Cadastrar seller', 'Listar todos os sellers', 'Buscar seller por id', 
               'Atualizar seller','Deletar seller', 'Rodar testes', 'Sair']
    print('\nMenu:')
    
    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')
    
    op = int(input('Escolha uma opção: '))
    return op
         

while True:
    try:
        op = menu()
        if op == 1:
            # new_seller()
            pass
        elif op == 2:
            # list_seller()
            pass
        elif op == 3:
            # read_by_id()
            pass
        elif op == 4:
            # product_detail()
            pass
        elif op == 5:
            # delete_product()
            pass
        elif op == 6:
            start_tests()
        elif op == 7:
            exit(0)
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')