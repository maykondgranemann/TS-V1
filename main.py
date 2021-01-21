import sys
sys.path.append('.')

from back.controllers.tests_controller import start_tests
from back.models.seller import Seller
from back.controllers.seller_controller import SellerController


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
        controller = SellerController()
        if op == 1:
            name = input("Informe o nome do seller: ")
            phone = input("Informe o telefone: ")
            email = input("Informe o e-mail: ")
            seller = Seller(name, phone, email)
            controller.save(seller)
            print(f'\nSeller {name} salvo.')
        elif op == 2:
            result = controller.read_all()
            for r in result:
                print(f'id: {r.id} - Nome: {r.name} - Telefone: {r.phone} - E-mail: {r.email}')
        elif op == 3:
            id = int(input("Informe o id: "))
            seller = controller.read_by_id(id)
            print(f'Nome: {seller.name} - Telefone: {seller.phone} - E-mail: {seller.email}')
        elif op == 4:
            id = int(input("Informe o id: "))
            seller = controller.read_by_id(id)
            print(seller.name, seller.phone, seller.email)
            seller.name = input('Informe o novo nome:')
            seller.phone = input('Informe o novo telefone:')
            seller.email = input('Informe o novo email:')
            controller.save(seller)
            print(f'Seller atualizado.')
        elif op == 5:
            id = int(input("Informe o id: "))
            seller = controller.read_by_id(id)
            print(f"""
                  Deseja realmente excluir?
                  Seller: {seller.name}
                  Telefone: {seller.phone}
                  E-mail: {seller.email}
                  """)
            check = int(input('[1] - Confirmar\n[2] - Calcelar: '))
            if check == 1:
                controller.delete(seller)
                print('\nExcluido...') 
            else:
                print('Cancelado')
        elif op == 6:
            start_tests()
        elif op == 7:
            exit(0)
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção precisa ser um numero inteiro listado.')