from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.seller import Seller


class SellerDao:
    def __init__(self):
        conector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills6'
        dbname = 'topskills6'
        password = 'olist123'
        conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"
        engine = create_engine(conn_string)
        Session = sessionmaker(engine)
        self.__session = Session()

    def create(self, model: Seller) -> None:
        self.__session.add(model)
        self.__session.commit()

    def update(self, model: Seller) -> None:
        self.__session.add(model)
        self.__session.commit()

    def read_all(self) -> list:
        result = self.__session.query(Seller).all()
        return result

    def read_by_id(self, id: int) -> Seller:
        model = self.__session.query(Seller).filter_by(id=id).first()
        return model

    def delete(self, model: Seller) -> None:
        self.__session.delete(model)
        self.__session.commit()



