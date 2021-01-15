from app.back.models.marketplace import Marketplace
from .base_dao import BaseDao

class MarketplaceDao(BaseDao):
    def create(self, model:Marketplace) -> None:
        query = f"""INSERT INTO marketplace 
                    (name, description) 
                    VALUES 
                    ('{model.name}', '{model.description}'); """
        super().execute(query)

    def read_by_id(self, id: int) -> Marketplace:
        query = f"SELECT id, name, description FROM marketplace WHERE id = {id};"
        result = super().read(query)[0]
        marketplace = Marketplace(result[1], result[2], result[0])
        return marketplace

    def read_all(self) -> list:
        query = f"SELECT id, name, description FROM marketplace;"
        result_list = super().read(query)
        marketplaces = []
        for result in result_list:
            marketplace = Marketplace(result[1],result[2] ,result[0])
            marketplaces.append(marketplace)
        return marketplaces

    def delete(self, id:int)->None:
            query = f"DELETE FROM marketplace WHERE id = {id};"
            super().execute(query)

    def update(self, model: Marketplace) -> None:
        query = f"UPDATE marketplace SET name = '{model.name}', description = '{model.description}' WHERE ID = {model.id};"
        super().execute(query)
