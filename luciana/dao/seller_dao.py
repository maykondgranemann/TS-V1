# from sqlalchemy.orm import sessionmaker
from luciana.dao.base_dao import BaseDao
from luciana.models.seller import Seller

#criação de classe para acessar o banco de dados
class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
