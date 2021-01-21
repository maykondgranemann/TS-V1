import sys
import random
sys.path.append('.')

from backend.controller.sellers_controller import SellerController
from backend.models.sellers import Seller



def menu():

    print('-' * 20 + '\nSellers \n\n 1)Salvar\n', '2) Mostrar BD \n', '3) Atualizar\n',
          '4) Deletar\n', '5) Sair\n')

    op = int(input('Selecione uma opção: '))
    return op

def main():
    while True:
        op=menu()
        x =random.randint(0,10000)
        if op==1:
            seller = Seller('Gustavo' + str(x), '345688888', 'ggggg@gmail.com')
            SellerController().save(seller)
        elif op==2:
            for s_aux in SellerController().read_all():
                print(s_aux)
        elif op==3:
            id_aux=int(input('Inseria um ID para buscar e atualizar:'))
            seller_aux=SellerController().read_by_id(id_aux)
            seller_aux.name=input('Novo nome:')
            seller_aux.phone =input('Novo Telefone')
            seller_aux.email = input('Novo Email')
            SellerController().save(seller_aux)
              
        elif op==4:
           id_aux=int(input('Inseria um ID para buscar e deletar:'))
           seller_aux=SellerController().read_by_id(id_aux)
           print(f'Linha deletada ->  {seller_aux}')
           SellerController().delete(seller_aux)
        elif op==5:
            exit(0)

main()