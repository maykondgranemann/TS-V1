import sys
sys.path.append('')
from sqlalchemy import Column, Integer
from model.base_model import BaseModel
from model.seller_model import Seller

seller = Seller

seller.name = input(str('Digite o nome do vendedor: '))
seller.phone = input(str('Agora o telefone: '))
seller.email = input(str('Para finalizar o e-mail: '))
seller.id = Column(Integer, primary_key = True)

print('Muito bem, dados cadastrados!')
print(seller.id, seller.name, seller.phone, seller.email)
