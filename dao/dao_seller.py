# Importar a da model a model_seller
from ..model.model_seller import Seller

# Importar da dao_base a classe DaoBase
from .dao_base import DaoBase

# Criar uma classe para acessar o BD 
class SellerDao(DaoBase):
    def __init__(self):
        super().__init__(Seller)


        

seller = Seller('novo seller', 'novo email', 'novo phone')

SellerDao().save(seller)

for s in SellerDao().read_all():
    print(s.id, s.name, s.email, s.phone)
