
from app.back.dao.base_dao import BaseDao
from app.back.models.seller import Seller

class SellerDao(BaseDao):
    def create(self, model: Seller) -> None:
        query = f"""INSERT INTO seller 
                    (name, telephone, email) 
                    VALUES 
                    ('{model.name}', '{model.telephone}', '{model.email}'); """
        super().execute(query)


    def read_by_id(self, id: int) -> Seller:
        query = f"SELECT name, telephone, email, id FROM seller WHERE id = {id};"
        result = super().read(query)[0]
        marketplace = Seller(result[0], result[1], result[2], result[3])
        return marketplace


    def read_all(self) -> list:
        query = f"SELECT id, name, telephone, email FROM seller;"
        result_list = super().read(query)
        sellers = []
        for result in result_list:
            seller = Seller(result[1], result[2], result[3], result[0])
            sellers.append(seller)
        return sellers


    def delete(self, id:int) -> None:
        query = f"DELETE FROM seller WHERE id = {id};"
        super().execute(query)


    def update(self, model: Seller) -> None:
        query = f"""UPDATE seller 
                    SET 
                        name = '{model.name}',
                        telephone = '{model.telephone}', 
                        email = '{model.email}' 
                    WHERE ID = {model.id};
                    """
        super().execute(query)
