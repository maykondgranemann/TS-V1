# Importar a da model a model_seller
from ..model.model_seller import Seller

# Criar uma classe para acessar o BD 
class SellerDao:
    def save(self, model:Seller):
        pass

    def read_all(self) -> list:
        pass

    def read_by_id(self, id_:int) -> Seller:
        pass

    def delete(self, id_:int) -> None:
        pass
