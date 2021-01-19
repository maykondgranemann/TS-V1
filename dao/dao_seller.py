# Importar a da model a model_seller
from ..model.model_seller import Seller

# Importar da dao_base a classe DaoBase
from .dao_base import DaoBase

# Importar a função da sessão através do session.py
from .session import Session

# Criar uma classe para acessar o BD 
class SellerDao(DaoBase):
    def __init__(self):
        pass
