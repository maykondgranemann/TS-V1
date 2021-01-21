# Importar a da model a model_seller
from model.model_seller import Seller

# Importar da dao_base a classe DaoBase
from dao.dao_base import DaoBase

# Criar uma classe para acessar o BD 
class SellerDao(DaoBase):
    def __init__(self):
        super().__init__(Seller)
