# Importar a da model a model_seller
from ..model.model_seller import Seller

# Importar a função da sessão através do session.py
from .session import Session

# Criar uma classe para acessar o BD 
class SellerDao:
    def save(self, model:Seller) -> None:
        self.__session.add(model)
        self.__session.commit()

    def read_all(self) -> list:
        return self.__session.query(Seller).all()

    def read_by_id(self, id_:int) -> Seller:
        return self.__session(Seller).filter_by(id=id).first()

    def delete(self, model: Seller) -> None:
        self.__session.delete(model)
        self.__session.commit()
