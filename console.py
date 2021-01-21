import sys
sys.path.append
from controller.seller_controller import SellerController
from model.base_model import Seller

seller = Seller
seller.name = input(str('Digite o nome do vendedor: '))
seller.phone = input(str('Agora o telefone: '))
seller.email = input(str('Para finalizar o e-mail: '))
print('Muito bem, dados cadastrados!')
print(seller.name, seller.phone, seller.email)
